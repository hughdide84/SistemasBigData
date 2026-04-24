from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, year, month, lpad

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("Ejercicio_Parquet_Sales") \
    .getOrCreate()

# Ruta del fichero CSV de entrada
input_path = "ficheros/sales.csv"

# Rutas de salida
output_parquet_unico = "ficheros/out/sales_parquet_unico"
output_parquet_particionado = "ficheros/out/sales_parquet_particionado"

# 1. Cargar el CSV
df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)

print("=== Esquema original ===")
df.printSchema()

print("=== Primeras filas ===")
df.show(5, truncate=False)

# 2. Convertir la columna de fecha y derivar año y mes
# El campo OrderDate viene con formato tipo: M/d/yyyy
df_transformado = df.withColumn(
    "OrderDate",
    to_date(col("OrderDate"), "M/d/yyyy")
).withColumn(
    "Year", year(col("OrderDate"))
).withColumn(
    "Month", month(col("OrderDate"))
)

print("=== Esquema transformado ===")
df_transformado.printSchema()

print("=== Muestra con Year y Month ===")
df_transformado.show(5, truncate=False)

# -------------------------------------------------
# CASO 1: Guardar todo en un único dataset Parquet
# -------------------------------------------------
df_transformado.write \
    .mode("overwrite") \
    .parquet(output_parquet_unico)

print(f"Parquet único generado en: {output_parquet_unico}")

# -------------------------------------------------
# CASO 2: Guardar en Parquet particionado por año y mes
# -------------------------------------------------
df_transformado.write \
    .mode("overwrite") \
    .partitionBy("Year", "Month") \
    .parquet(output_parquet_particionado)

print(f"Parquet particionado generado en: {output_parquet_particionado}")

# -------------------------------------------------
# Comprobación de lectura de ambos resultados
# -------------------------------------------------
print("=== Lectura del Parquet único ===")
df_parquet_unico = spark.read.parquet(output_parquet_unico)
df_parquet_unico.show(5, truncate=False)

print("=== Lectura del Parquet particionado ===")
df_parquet_particionado = spark.read.parquet(output_parquet_particionado)
df_parquet_particionado.show(5, truncate=False)

# Finalizar sesión
spark.stop()