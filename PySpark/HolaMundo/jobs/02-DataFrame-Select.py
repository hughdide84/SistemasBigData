# Importa SparkSession y funciones para trabajar con columnas
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Crea la SparkSession
spark = SparkSession.builder.appName("EjemploSELECT").getOrCreate()

# Define datos de ejemplo y crea el DataFrame
datos = [(1, "Juan", 1200), (2, "Ana", 1500), (3, "Pedro", 1000)]
columnas = ["id", "nombre", "ventas"]
df = spark.createDataFrame(datos, columnas)
df.show()

# Selecciona solo las columnas nombre y ventas
df_select = df.select("nombre", "ventas")
df_select.show()

# Calcula una nueva columna aplicando IVA a las ventas
df_calculado = df.select(
    "nombre",
    "ventas",
    (col("ventas") * 1.21).alias("ventas_con_iva")
)
df_calculado.show()