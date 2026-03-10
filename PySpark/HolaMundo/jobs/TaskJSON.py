from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.appName("usuarios_clean").getOrCreate()

# Leer JSON
df = spark.read.json("./ficheros/usuarios.json")

print("Registros originales:", df.count())
df.show(truncate=False)

# -------------------------
# 1. Limpiar emails
# -------------------------
df = df.withColumn(
    "email",
    lower(trim(col("email")))
)

# Si email es null lo dejamos como "unknown"
df = df.fillna({"email": "unknown@mail.com"})

# -------------------------
# 2. Convertir edad
# -------------------------
df = df.withColumn(
    "edad",
    expr("try_cast(edad as int)")
)

# -------------------------
# 3. Normalizar país
# -------------------------
df = df.withColumn(
    "pais",
    initcap(trim(col("pais")))
)

# -------------------------
# 4. Convertir timestamp
# -------------------------
df = df.filter(col("timestamp").isNotNull())
df = df.withColumn(
    "timestamp_clean",
    coalesce(
        expr("try_to_timestamp(timestamp, 'yyyy-MM-dd HH:mm:ss')"),
        expr("try_to_timestamp(timestamp, 'dd-MM-yyyy HH:mm:ss')"),
        expr("try_to_timestamp(timestamp, 'yyyy/MM/dd HH:mm:ss')"),
        expr("try_to_timestamp(timestamp, 'yyyy-MM-dd''T''HH:mm:ss')")
    )
)

# -------------------------
# 5. Eliminar duplicados
# -------------------------
df = df.dropDuplicates(["id_usuario"])

# -------------------------
# 6. Validar edades (0-120)
# -------------------------
df_valid = df.filter((col("edad") >= 0) & (col("edad") <= 120))

# -------------------------
# 7. Dataset final
# -------------------------
usuarios_clean = df_valid

usuarios_clean.show()

# -------------------------
# RESPUESTAS
# -------------------------

usuarios_unicos = usuarios_clean.count()

edad_media = usuarios_clean.select(avg("edad")).first()[0]

edad_fuera_rango = df.filter(
    (col("edad") < 0) | (col("edad") > 120)
).count()

registros_eliminados = df.count() - usuarios_clean.count()

print("Usuarios únicos:", usuarios_unicos)
print("Edad media:", edad_media)
print("Registros fuera de rango:", edad_fuera_rango)
print("Registros eliminados:", registros_eliminados)