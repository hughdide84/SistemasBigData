from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, month, when
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier

# 1. Crear sesión
spark = SparkSession.builder.appName("RF_Simple").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# 2. Cargar datos
df = spark.read.csv("ficheros/sales.csv", header=True, inferSchema=True)

# 3. Preparar datos
df = df.withColumn("OrderDate", to_date(col("OrderDate")))

# Calcular importe total
df = df.withColumn(
    "importe_total",
    (col("Quantity") * col("UnitPrice")) + col("TaxAmount")
)

# Crear variable objetivo
df = df.withColumn(
    "tipo_venta",
    when(col("importe_total") > 1000, "Alta").otherwise("Normal")
)

# Sacar el mes
df = df.withColumn("mes", month(col("OrderDate")))

# 4. Convertir variables categóricas a numéricas

item_indexer = StringIndexer(inputCol="Item", outputCol="ItemIndex")
df = item_indexer.fit(df).transform(df)

label_indexer = StringIndexer(inputCol="tipo_venta", outputCol="label")
label_model = label_indexer.fit(df)
df = label_model.transform(df)

# Ver valores
print(label_model.labels)

# 5. Crear vector de características
assembler = VectorAssembler(
    inputCols=["Quantity", "UnitPrice", "mes", "ItemIndex"],
    outputCol="features"
)

df = assembler.transform(df)
df.select(
    "Quantity",
    "UnitPrice",
    "mes",
    "ItemIndex",
    "importe_total",
    "tipo_venta").show()

# 6. Modelo Random Forest
rf = RandomForestClassifier(
    labelCol="label",
    featuresCol="features",
    numTrees=50,
    maxBins=150,
    seed=1
)

model = rf.fit(df)

# 7. Predicciones
predictions = model.transform(df)

# 8. Ver resultados
predictions.select(
    "Quantity",
    "UnitPrice",
    "importe_total",
    "mes",
    "ItemIndex",
    "tipo_venta",
    "prediction"
).show(20)

# 9. Cerrar sesión
spark.stop()