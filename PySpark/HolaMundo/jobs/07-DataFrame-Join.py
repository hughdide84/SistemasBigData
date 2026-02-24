# Importa SparkSession
from pyspark.sql import SparkSession

# Crea la SparkSession
spark = SparkSession.builder.appName("EjemploJOIN").getOrCreate()

# Define datos de empleados y crea el DataFrame principal
datos = [
    (1, "Juan", "Ventas", 1200),
    (2, "Ana", "Ventas", 1500),
    (3, "Pedro", "IT", 1000),
    (4, "Lucia", "IT", 1800)
]
columnas = ["id", "nombre", "departamento", "ventas"]
df = spark.createDataFrame(datos, columnas)
df.show()

# Define datos de departamentos y crea el DataFrame auxiliar
datos_dept = [("Ventas", "Madrid"), ("IT", "Barcelona")]
columnas_dept = ["departamento", "ciudad"]
df_departamentos = spark.createDataFrame(datos_dept, columnas_dept)
df_departamentos.show()

# Realiza un join interno entre empleados y departamentos
df_join = df.join(
    df_departamentos,
    on="departamento",
    how="inner"
)
df_join.show()