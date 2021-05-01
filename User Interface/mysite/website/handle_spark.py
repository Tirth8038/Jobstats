import pyspark
from pyspark.sql import SQLContext,SparkSession
from pyspark import SparkContext,SparkConf

class Spark_handle():

    sc = pyspark.SparkContext('local[*]')
    sqlcontext = SQLContext(sc)
    histogram = sqlcontext.read.csv("salary_histogram.csv",header = True).rdd
    job_location = sqlcontext.read.csv("jobcount_by_location.csv",header = True).rdd
    job_company = sqlcontext.read.csv("jobcount_by_company.csv",header = True).rdd
