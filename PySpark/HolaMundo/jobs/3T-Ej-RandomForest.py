from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.sql.functions import round, col
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


# Crear sesión
spark = SparkSession.builder.appName("ClasificacionBasica").getOrCreate()

# Datos de ejemplo:
# visitas, compra
# 0 = no compra
# 1 = compra
datos = [
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),  
    (8, 0),  
    (9, 0)       
]

df = spark.createDataFrame(datos, ["visitas", "compra"])

# Convertir la variable de entrada a features
assembler = VectorAssembler(inputCols=["visitas"], outputCol="features")
df2 = assembler.transform(df)
df2.show()

# Crear el modelo
lr = LogisticRegression(featuresCol="features", labelCol="compra")

# Entrenar
modelo = lr.fit(df2)

# Probar sobre los mismos datos
predicciones = modelo.transform(df2)
predicciones.select("visitas", "compra", "prediction", ).show(truncate=False)

# Predecir un nuevo caso
nuevo = spark.createDataFrame([(19,)], ["visitas"])
nuevo2 = assembler.transform(nuevo)

pred_nueva = modelo.transform(nuevo2)
pred_nueva.show()
pred_nueva.select("visitas", "prediction",  "probability").show(truncate=False)

# Evaluar
evaluator = MulticlassClassificationEvaluator(
    labelCol="compra",
    predictionCol="prediction",
    metricName="accuracy"
)

accuracy = evaluator.evaluate(predicciones)

print("Accuracy:", accuracy)

spark.stop()