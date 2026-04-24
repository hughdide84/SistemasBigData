from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    to_date,
    year,
    month,
    sum as _sum,
    count,
    avg,
    max as _max,
    min as _min,
    round as _round,
    countDistinct
)

spark = SparkSession.builder \
    .appName("KPIs_Sales_PySpark") \
    .getOrCreate()

input_path = "ficheros/sales.csv"

# Cargar CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(input_path)

# Crear fecha + año + mes + importe venta
df_preparado = df.withColumn(
    "Year",
    year(col("OrderDate"))
).withColumn(
    "Month",
    month(col("OrderDate"))
).withColumn(
    "ImporteVenta",
    col("Quantity") * col("UnitPrice")
)

# KPIs agrupados por año y mes
df_resumen = df_preparado.groupBy("Year", "Month").agg(
    _round(_sum("ImporteVenta"), 2).alias("Ventas"),
    count("*").alias("Operaciones"),
    _round(avg("ImporteVenta"), 2).alias("TM"),
    _round(_max("ImporteVenta"), 2).alias("MaxVentas"),
    _round(_min("ImporteVenta"), 2).alias("MinVentas"),

    # KPIs adicionales
    countDistinct("CustomerName").alias("Clientes"),
    _round(avg("Quantity"), 2).alias("Cantidad"),
    _round(_sum("TaxAmount"), 2).alias("Impuestos")
).orderBy("Year", "Month")

# Mostrar resultados
df_resumen.show(100, truncate=False)

spark.stop()