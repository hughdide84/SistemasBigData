from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, trim, lower, upper, initcap, regexp_replace, coalesce,
    to_date, when, lit, avg, count, try_to_date
)
from pyspark.sql.types import DoubleType, IntegerType

# Crear sesión
spark = SparkSession.builder.appName("LimpiezaVentas").getOrCreate()

# 1) Cargar CSV
df = (
    spark.read
    .option("header", True)
    .option("inferSchema", False)
    .csv("./ficheros/ventas.csv")
)

print("=== Esquema original ===")
df.printSchema()

print("=== Datos originales ===")
df.show(truncate=False)

# 2) Limpieza de textos
df_clean = (
    df.withColumn("cliente", when(col("cliente").isNull(), lit("Desconocido")).otherwise(initcap(trim(col("cliente")))))
      .withColumn("ciudad", initcap(trim(col("ciudad"))))
      .withColumn("producto", lower(trim(col("producto"))))
)

# 3) Conversión de tipos
# id_venta y unidades
df_clean = (
    df_clean.withColumn("id_venta", col("id_venta").cast(IntegerType()))
            .withColumn("unidades", col("unidades").cast(IntegerType()))
)

# precio: reemplazar coma por punto y convertir a double
df_clean = (
    df_clean.withColumn("precio_str", regexp_replace(trim(col("precio")), ",", "."))
            .withColumn("precio_num", col("precio_str").try_cast(DoubleType()))
)

# fecha: intentar varios formatos
df_clean = (
    df_clean.withColumn(
        "fecha_clean",
        coalesce(
            try_to_date(col("fecha"), "yyyy-MM-dd"),
            try_to_date(col("fecha"), "dd/MM/yyyy"),
            try_to_date(col("fecha"), "yyyy/MM/dd"),
            try_to_date(col("fecha"), "dd-MM-yyyy")
        )
    )
)

print("=== Tras normalización ===")
df_clean.show(truncate=False)

# 4) Eliminar inválidos
# Reglas:
# - precio no nulo
# - precio >= 0
# - fecha válida
# - unidades > 0
df_valid = (
    df_clean.filter(col("precio_num").isNotNull())
            .filter(col("precio_num") >= 0)
            .filter(col("fecha_clean").isNotNull())
            .filter(col("unidades") > 0)
)

print("=== Registros válidos antes de quitar duplicados ===")
df_valid.show(truncate=False)

# 5) Eliminar duplicados por id_venta
ventas_clean = df_valid.dropDuplicates(["id_venta"])

print("=== Dataset final ventas_clean ===")
ventas_clean.show(truncate=False)

# 6) Respuestas
registros_validos = ventas_clean.count()
precio_medio = ventas_clean.select(avg("precio_num").alias("precio_medio")).collect()[0]["precio_medio"]
precios_negativos = ventas_clean.filter(col("precio_num") < 0).count()

print("=== RESULTADOS ===")
print(f"Registros válidos finales: {registros_validos}")
print(f"Precio medio: {precio_medio:.2f}")
print(f"¿Existen precios negativos en el dataset final?: {'Sí' if precios_negativos > 0 else 'No'}")

# 7) Seleccionar columnas finales
ventas_clean = ventas_clean.select(
    "id_venta",
    "cliente",
    "ciudad",
    "producto",
    col("precio_num").alias("precio"),
    "unidades",
    col("fecha_clean").alias("fecha")
)


