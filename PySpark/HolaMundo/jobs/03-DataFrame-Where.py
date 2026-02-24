# Importa SparkSession y funciones para trabajar con columnas
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Crea la SparkSession
spark = SparkSession.builder.appName("EjemploWHERE").getOrCreate()

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

# Filtra filas usando condiciones tipo SQL con AND
df_sql = df.where("ventas > 1500 AND departamento = 'Ventas'")
df_sql.show()

# Filtra filas usando condiciones tipo SQL con OR
df_sql_or = df.where("ventas > 1500 OR departamento = 'IT'")
df_sql_or.show()