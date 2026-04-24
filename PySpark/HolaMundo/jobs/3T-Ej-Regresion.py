from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql.functions import round


# Crear sesión de Spark
spark = SparkSession.builder.appName("RegresionLinealBasica").getOrCreate()

# Datos de ejemplo
datos = [
    (50, 100000),
    (60, 110000),
    (70, 170000),
    (80, 130000),
    (90, 140000)
]

# Crear DataFrame
df = spark.createDataFrame(datos, ["metros", "precio"])

# Convertir la variable x en vector (obligatorio en MLlib)
assembler = VectorAssembler(inputCols=["metros"], outputCol="features")
df_vector = assembler.transform(df)
df_vector.show()

# Crear modelo de regresión lineal
lr = LinearRegression(featuresCol="features", labelCol="precio")

# Entrenar modelo
modelo = lr.fit(df_vector)

# Mostrar resultados
print("Pendiente:", modelo.coefficients[0])
print("Intercepto:", modelo.intercept)

# Hacer predicciones
predicciones = modelo.transform(df_vector)
predicciones.select("metros", "precio", round("prediction", 2).alias("estimacion")).show()

# Nuevo valor fuera de la muestra
nuevo = spark.createDataFrame([(200,)], ["metros"])
nuevo_vector = assembler.transform(nuevo)
prediccion = modelo.transform(nuevo_vector)
prediccion.select("metros", round("prediction", 2).alias("estimacion")).show()

# Indicadores
print("R2:", modelo.summary.r2)
print("RMSE:", modelo.summary.rootMeanSquaredError)
print("MAE:", modelo.summary.meanAbsoluteError)

spark.stop()