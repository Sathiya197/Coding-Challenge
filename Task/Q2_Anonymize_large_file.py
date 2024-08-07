from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2

spark = SparkSession.builder \
    .appName("Anonymize Data") \
    .getOrCreate()

schema = "first_name STRING, last_name STRING, address STRING, date_of_birth DATE"

df = spark.read.csv('data.csv', header=True, schema=schema)

anonymized_df = df.withColumn('first_name', sha2(df.first_name, 256)) \
                  .withColumn('last_name', sha2(df.last_name, 256)) \
                  .withColumn('address', sha2(df.address, 256))

anonymized_df.write.csv('anonymized_large.csv', header=True, mode='overwrite')

spark.stop()
