from pyspark.sql import SparkSession

# Crear la SparkSession con el paquete spark-excel
spark = (
    SparkSession.builder
    .appName("LeerExcel")
    .config("spark.jars.packages", "com.crealytics:spark-excel_2.13:3.5.1_0.20.4")
    .getOrCreate()
)

try:
    df = (
        spark.read
        .format("com.crealytics.spark.excel")
        .option("header", "true")
        .option("inferSchema", "true")           
        .option("dataAddress", "'Sheet1'!")
        .option("treatEmptyValuesAsNulls", "true")
        .load("ficheros/fichero.xlsx")
    )

    # Mostrar datos
    df.show()

    # Mostrar esquema
    df.printSchema()

except Exception as e:
    print("Error al leer el fichero Excel:", e)

# Cerrar Spark
spark.stop()