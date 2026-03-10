from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("LeerCSV") \
    .getOrCreate()

try:
    df = (
        spark.read
        .option("header", "true")        # el CSV tiene cabecera
        .option("inferSchema", "true")   # infiere tipos
        .option("delimiter", ",")        # separador
        .csv("ficheros/fichero.csv")
    )

    df.show()
    df.printSchema()
except Exception as e:
    print("Error al leer el fichero:", e)

spark.stop()