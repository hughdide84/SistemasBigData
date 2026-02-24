# Importa Spark y utilidades de tiempo
from pyspark.sql import SparkSession
import time

# Crea la SparkSession (punto de entrada a Spark)
spark = SparkSession.builder \
    .appName("HolaMundoPySpark") \
    .getOrCreate()

# Muestra información básica del contexto Spark
print("master =", spark.sparkContext.master)
print("appId  =", spark.sparkContext.applicationId)

# Pausa la ejecución para observar el estado del job
print("Spark iniciado. Esperando 15 segundos antes de ejecutar el job...")
time.sleep(15)

# Mensaje simple para verificar la ejecución del programa
print("Hola mundo desde PySpark 👋")

# Detiene la SparkSession y libera recursos
spark.stop()