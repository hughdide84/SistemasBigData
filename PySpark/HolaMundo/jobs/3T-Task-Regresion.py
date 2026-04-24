from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    to_date,
    year,
    month,
    sum as _sum,
    lit
)

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# Crear sesión Spark
spark = SparkSession.builder \
    .appName("Regresion_Lineal_Ventas_Mensuales") \
    .getOrCreate()

input_path = "ficheros/sales.csv"

# -----------------------------
# 1. Cargar CSV
# -----------------------------
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(input_path)

print("=== Datos originales ===")
df.show(5, truncate=False)

# -----------------------------
# 2. Calcular importe total operación
# -----------------------------
df_preparado = df.withColumn(
    "OrderDate",
    to_date(col("OrderDate"), "yyyy-MM-dd")
).withColumn(
    "Year",
    year(col("OrderDate"))
).withColumn(
    "Month",
    month(col("OrderDate"))
).withColumn(
    "ImporteOperacion",
    (col("Quantity") * col("UnitPrice")) + col("TaxAmount")
)

print("=== Datos con importe operación ===")
df_preparado.select(
    "OrderDate",
    "Quantity",
    "UnitPrice",
    "TaxAmount",
    "ImporteOperacion"
).show(5, truncate=False)

# -----------------------------
# 3. Dataset agregado por año y mes
# -----------------------------
df_mensual = df_preparado.groupBy("Year", "Month").agg(
    _sum("ImporteOperacion").alias("VentasMensuales")
).orderBy("Year", "Month")

print("=== Ventas mensuales ===")
df_mensual.show(100, truncate=False)

# -----------------------------
# 4. Variable temporal numérica
# -----------------------------
# Índice temporal secuencial para el modelo
ventas_lista = df_mensual.collect()

datos_modelo = []
for i, fila in enumerate(ventas_lista):
    datos_modelo.append((i + 1, fila["VentasMensuales"]))

df_modelo = spark.createDataFrame(
    datos_modelo,
    ["Periodo", "VentasMensuales"]
)

print("=== Dataset para modelo ===")
df_modelo.show()

# -----------------------------
# 5. Preparar features MLlib
# -----------------------------
assembler = VectorAssembler(
    inputCols=["Periodo"],
    outputCol="features"
)

df_features = assembler.transform(df_modelo)

# -----------------------------
# 6. Crear modelo regresión lineal
# -----------------------------
lr = LinearRegression(
    featuresCol="features",
    labelCol="VentasMensuales"
)

modelo = lr.fit(df_features)

print("=== Parámetros modelo ===")
print(f"Intercepto: {modelo.intercept}")
print(f"Pendiente: {modelo.coefficients[0]}")

# -----------------------------
# 7. Predicción siguiente mes
# -----------------------------
ultimo_periodo = df_modelo.agg({"Periodo": "max"}).collect()[0][0]
siguiente_mes = ultimo_periodo + 1

df_pred = spark.createDataFrame(
    [(siguiente_mes,)],
    ["Periodo"]
)

df_pred_features = assembler.transform(df_pred)

prediccion = modelo.transform(df_pred_features)

print("=== Predicción siguiente mes ===")
prediccion.select("Periodo", "prediction").show()

# -----------------------------
# 8. Predicciones históricas
# -----------------------------
print("=== Ajuste sobre histórico ===")
historico_pred = modelo.transform(df_features)
historico_pred.select(
    "Periodo",
    "VentasMensuales",
    "prediction"
).show()

# -----------------------------
# 9. Validar
# -----------------------------
modelo = lr.fit(df_features)

# Calcular métricas del modelo
r2 = modelo.summary.r2
rmse = modelo.summary.rootMeanSquaredError
mae = modelo.summary.meanAbsoluteError

print("=== Métricas del modelo ===")
print(f"R²: {r2:.4f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")

spark.stop()