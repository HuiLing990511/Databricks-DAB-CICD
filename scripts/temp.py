from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.remote(cluster_id="0619-071005-rh3oj15u").getOrCreate()
spark.sql("SELECT 1").show()
