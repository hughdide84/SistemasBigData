import requests
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LeerAPI") \
    .getOrCreate()

try:
    url = "https://api.sampleapis.com/baseball/hitsSingleSeason"

    response = requests.get(url, timeout=30)
    response.raise_for_status()  

    data = response.json()  

    df = spark.createDataFrame(data)

    df.show()
    df.printSchema()

except Exception as e:
    print("Error al leer la API:", e)

spark.stop()