from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LeerJSON") \
    .getOrCreate()

try:
    df = spark.read.option("multiline","true").json("ficheros/fichero.json")

    df.show(truncate=False)
    df.printSchema()

except Exception as e:
    print("Error al leer el fichero:", e)

spark.stop()