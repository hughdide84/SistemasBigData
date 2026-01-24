from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("HolaMundoPySpark") \
    .getOrCreate()

print("master =", spark.sparkContext.master)
print("appId  =", spark.sparkContext.applicationId)

print("Spark iniciado. Esperando 15 segundos antes de ejecutar el job...")
time.sleep(15)

print("Hola mundo desde PySpark 👋")

spark.stop()