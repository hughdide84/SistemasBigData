from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LeerBD") \
    .config("spark.jars.packages", "org.mariadb.jdbc:mariadb-java-client:3.3.3") \
    .getOrCreate()

try:
    host_name = 'host.docker.internal'
    database_name = 'prueba'
    user_name = 'root'
    password = 'ADMIN0'
    port = '3306'
    sql = "SELECT * FROM usuarios"
    jdbc_url = f"jdbc:mysql://{host_name}:{port}/{database_name}?permitMysqlScheme"
    df = spark.read \
        .format("jdbc") \
        .option("driver", "org.mariadb.jdbc.Driver") \
        .option("url", jdbc_url) \
        .option("query", sql) \
        .option("user", user_name) \
        .option("password", password) \
        .load()

    df.show(truncate=False) 
    df.printSchema()

except Exception as e:
    print("Error al leer MariaDB:", e)

spark.stop()