from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LeerXML") \
    .getOrCreate()

try:
    df = (spark.read
          .format("xml")
          .option("rowTag", "persona")  
          .option("inferSchema", "true")
          .load("ficheros/fichero.xml"))

    df.show(truncate=False)
    df.printSchema()

except Exception as e:
    print("Error al leer el fichero:", e)

spark.stop()