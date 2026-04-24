from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# --------------------------------------------------
# 1. Crear sesión Spark
# --------------------------------------------------
spark = SparkSession.builder.appName("KMeansBasico").getOrCreate()

# --------------------------------------------------
# 2. Datos de ejemplo
#    edad, gasto
# --------------------------------------------------
datos = [
    (25, 200),
    (27, 220),
    (30, 250),
    (32, 270),
    (40, 800),
    (42, 820),
    (45, 850),
    (48, 900)
]

df = spark.createDataFrame(datos, ["edad", "gasto"])

print("Datos originales:")
df.show()

# --------------------------------------------------
# 3. Convertir columnas de entrada en vector features
# --------------------------------------------------
assembler = VectorAssembler(
    inputCols=["edad", "gasto"],
    outputCol="features"
)

df_features = assembler.transform(df)

print("Datos con features:")
df_features.select("edad", "gasto", "features").show(truncate=False)

# --------------------------------------------------
# 4. Crear modelo KMeans
#    k=2 porque queremos 2 grupos
# --------------------------------------------------
kmeans = KMeans(
    featuresCol="features",
    predictionCol="prediction",
    k=3,
    seed=1
)

# --------------------------------------------------
# 5. Entrenar modelo
# --------------------------------------------------
modelo = kmeans.fit(df_features)

# --------------------------------------------------
# 6. Obtener predicciones
# --------------------------------------------------
predicciones = modelo.transform(df_features)

print("Predicciones:")
predicciones.select("edad", "gasto", "prediction").show()

# --------------------------------------------------
# 7. Mostrar centros de los clusters
# --------------------------------------------------
centros = modelo.clusterCenters()

print("Centros de los clusters:")
for i, centro in enumerate(centros):
    print(f"Cluster {i}: {centro}")

# --------------------------------------------------
# 8. Evaluar caso
# --------------------------------------------------
nuevo = spark.createDataFrame([(33, 260)], ["edad", "gasto"])
nuevo_features = assembler.transform(nuevo)
pred_nuevo = modelo.transform(nuevo_features)
pred_nuevo.select("edad", "gasto", "prediction").show()

# --------------------------------------------------
# 9. Evaluación del clustering
#    Métrica: Silhouette
#    1 - Excelente
#    0 - Regular
#    < 0 - Mala
# --------------------------------------------------
evaluator = ClusteringEvaluator(
    featuresCol="features",
    predictionCol="prediction",
    metricName="silhouette",
    distanceMeasure="squaredEuclidean"
)

silhouette = evaluator.evaluate(predicciones)

print("Silhouette =", silhouette)

spark.stop()