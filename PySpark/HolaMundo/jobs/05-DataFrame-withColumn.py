# Importa SparkSession y funciones para trabajar con columnas y condiciones
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Crea la SparkSession
spark = SparkSession.builder.appName("EjemploCOLUMN").getOrCreate()

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

# Crea una nueva columna categorizando el nivel de ventas
df_nuevo = df.withColumn(
    "nivel_ventas",
    when(col("ventas") >= 1500, "Alto")
     .when(col("ventas") >= 1200, "Medio")
     .otherwise("Bajo")
)

df_nuevo.show()