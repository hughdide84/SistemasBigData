from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LeerFIchero") \
    .getOrCreate()

try:
    df = spark.read.text("ficheros/fichero.txt")
    df.show(5)
except Exception as e:
    print("Error al leer el fichero:", e)

spark.stop()