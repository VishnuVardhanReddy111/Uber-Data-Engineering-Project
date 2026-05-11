# from pyspark import pipelines as dp
# from pyspark.sql.functions import *

# EH_NAMESPACE = "UberEventsVishnu"
# EH_NAME = "ubertopic"

# # Read connection string
# # EH_CONN_STR = ""

# KAFKA_OPTIONS = {
#     "kafka.bootstrap.servers":
#         f"<Event>.servicebus.windows.net:9093",

#     "subscribe": "",

#     "kafka.security.protocol": "SASL_SSL",

#     "kafka.sasl.mechanism": "PLAIN",

#     "kafka.sasl.jaas.config":
#         'kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required '
#         f'username="$ConnectionString" '
#         f'password="";',

#     "startingOffsets": "earliest",

#     "failOnDataLoss": "false"
# }

# @dp.table
# def rides_raw():

#     return (
#         #readStream
#         spark.read
#         .format("kafka")
#         .options(**KAFKA_OPTIONS)
#         .load()
#         .select(
#             col("value").cast("string").alias("rides"),
#             col("timestamp")
#         )
#     )
