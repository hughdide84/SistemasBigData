# Importa SparkSession y funciones para trabajar con columnas
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Crea la SparkSession
spark = SparkSession.builder.appName("EjemploORDER").getOrCreate()

# Define datos de ejemplo y crea el DataFrame
datos = [
    (1, "Juan", "Ventas", 1200),
    (2, "Ana", "Ventas", 1500),
    (3, "Pedro", "IT", 1000),
    (4, "Lucia", "IT", 1800)
]
columnas = ["id", "nombre", "departamento", "ventas"]
df = spark.createDataFrame(datos, columnas)
df.show()

# Ordena el DataFrame por ventas en orden ascendente
df.orderBy("ventas").show()

# Ordena el DataFrame por ventas en orden descendente
df.orderBy(col("ventas").desc()).show()

# Ordena el DataFrame por departamento y ventas descendentes
df.orderBy("departamento", col("ventas").desc()).show()