from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col, to_timestamp, from_unixtime

spark = (
    SparkSession.builder
    .appName("LeerSTREAM")
    .getOrCreate()
)

dfs = (
    spark.readStream.format("socket")
    .option("host", "host.docker.internal")
    .option("port", 7777).load()
)

dfs_parsed = (
    dfs
    .withColumn("temp", split(col("value"), ",").getItem(0).cast("int"))
    .withColumn("epoch", split(col("value"), ",").getItem(1).cast("double"))
    .withColumn("event_time",to_timestamp(from_unixtime(col("epoch")))
    ).select("temp", "event_time")
)

con = (
    dfs_parsed.writeStream
    .outputMode("append").format("console").start()
)

con.awaitTermination()