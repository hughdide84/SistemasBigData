from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, regexp_replace, trim

spark = (
    SparkSession.builder
    .appName("LeerEXCEL")
    .config("spark.jars.packages", "com.crealytics:spark-excel_2.13:3.5.1_0.20.4")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

try:
    df = (
        spark.read
        .format("com.crealytics.spark.excel")
        .option("header", "true")
        .option("inferSchema", "true")             
        .option("dataAddress", "'Sheet1'!A1")    
        .option("treatEmptyValuesAsNulls", "true")
        .load("ficheros/fichero.xlsx")
    )

    # Limpieza y casteo de Units Sold a double (por si viene con coma decimal o espacios)
    df2 = (
        df
        .withColumn("Country", trim(col("Country")))
        .withColumn(
            "Units Sold",
            regexp_replace(trim(col("Units Sold")), ",", ".").cast("double")
        )
    )

    # Agrupar por país y sumar unidades
    resultado = (
        df2.groupBy("Country")
           .agg(_sum(col("Units Sold")).alias("Total Units Sold"))
           .orderBy(col("Total Units Sold").desc())   # opcional: ordenar
    )

    resultado.show(truncate=False)

except Exception as e:
    print("Error:", e)

spark.stop()