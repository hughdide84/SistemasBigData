# Importa SparkSession y funciones de agregación
from pyspark.sql import SparkSession
from pyspark.sql.functions import count, sum, avg

# Crea la SparkSession
spark = SparkSession.builder.appName("EjemploGROUP").getOrCreate()

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

# Agrupa por departamento y calcula suma y media de ventas
df_group = df.groupBy("departamento").agg(
    sum("ventas").alias("total_ventas"),
    avg("ventas").alias("promedio_ventas")
)
df_group.show()

# Agrupa por departamento y cuenta el número de empleados
df_count = df.groupBy("departamento").agg(
    count("*").alias("cantidad_empleados")
)
df_count.show()