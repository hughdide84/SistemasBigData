from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum, count
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# 1. Crear sesión
spark = SparkSession.builder.appName("KMeans_Clientes").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# 2. Cargar datos
df = spark.read.csv("ficheros/sales.csv", header=True, inferSchema=True)

# 3. Calcular importe total de cada operación
df = df.withColumn(
    "importe_total",
    (col("Quantity") * col("UnitPrice")) + col("TaxAmount")
)

# 4. Agrupar por cliente
clientes = df.groupBy("CustomerName").agg(
    count("*").alias("num_operaciones"),
    sum("importe_total").alias("importe_total_acumulado"),
    avg("importe_total").alias("ticket_medio"),
    sum("Quantity").alias("cantidad_total_productos")
)

# 5. Crear vector de características
assembler = VectorAssembler(
    inputCols=[
        "num_operaciones",
        "importe_total_acumulado",
        "ticket_medio",
        "cantidad_total_productos"
    ],
    outputCol="features"
)

clientes = assembler.transform(clientes)

# 6. Aplicar KMeans
kmeans = KMeans(
    k=3,                 
    seed=1,
    featuresCol="features",
    predictionCol="prediction"
)

model = kmeans.fit(clientes)

# 7. Obtener predicciones
predicciones = model.transform(clientes)

# 8. Mostrar resultados
predicciones.select(
    "CustomerName",
    "num_operaciones",
    "importe_total_acumulado",
    "ticket_medio",
    "cantidad_total_productos",
    "prediction"
).show(20, truncate=False)

# 9. Mostrar centros de los clusters
print(f"------------------")
print("Centros de los clusters:")
for i, centro in enumerate(model.clusterCenters()):
    print(f"Cluster {i}: {centro}")

# 10. Evaluar
evaluator = ClusteringEvaluator(
    featuresCol="features",
    predictionCol="prediction",
    metricName="silhouette"
)

score = evaluator.evaluate(predicciones)
print(f"------------------")
print(f"Silhouette={score}")

spark.stop()