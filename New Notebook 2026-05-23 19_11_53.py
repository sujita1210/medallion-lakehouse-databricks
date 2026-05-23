# Databricks notebook source
display(dbutils.fs.ls("dbfs:/Volumes/workspace/default/project1"))

# COMMAND ----------

#Bronze Layer RAW Data Ingestion
from pyspark.sql import functions as F

# Defining Paths
RAW_PATH    = "dbfs:/FileStore/nyc_taxi/raw/"
BRONZE_PATH = "dbfs:/FileStore/nyc_taxi/bronze/"
BRONZE_TABLE = "nyc_taxi_bronze"
