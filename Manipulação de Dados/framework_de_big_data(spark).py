# -*- coding: utf-8 -*-
"""Framework de Big Data(Spark)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H5yW_ZfIy2i856ZWHgljJfNKKOwHDOJz

##1  PySpark - Instalando a biblioteca no google colab
"""

!pip install pyspark

!pip install findspark

import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()

df=spark.sql('''select 'Sucesso total, estamos online!' as hello''')
df.show()

#importando as bibliotecas do spark
from pyspark.sql import Row, DataFrame
from pyspark.sql.types import StringType, StructType, StructField, IntegerType
from pyspark.sql.functions import col, expr, lit, substring, concat, concat_ws, when, coalesce
from pyspark.sql import functions as F #for more SQL functions
from functools import reduce

"""##2 Data Manipulations using Spark"""

df=spark.read.csv("/content/banklist.csv", sep=",", inferSchema=True, header=True)

print("df.count: ", df.count())
print("df.col ct: ", len(df.columns))
print("df.columns: ", df.columns)

"""##3 Using SQL in PySpark"""

df.createOrReplaceTempView("banklist")
df_check=spark.sql('''select `Bank Name`, city, `Closing Date` from banklist''')
df_check.show()

df.createOrReplaceTempView("banklist")
df_check=spark.sql('''select `Bank Name`, city, `Closing Date` from banklist''')
df_check.show(4, truncate=False)

"""##4 DataFrame Basic Operations"""

df.describe().show()

df.describe("City", "ST").show()

"""Count, Columns and Schema"""

print("total de Linhas: ", df.count())
print("total de Colunas: ", len(df.columns))
print("Colunas: ", df.columns)
print("Tipo do Dado: ", df.dtypes)
print("Schema: ", df.schema)

df.printSchema()

"""##5 Remove Duplicates"""

df=df.dropDuplicates()
print("df.count: ", df.count())
print("df.columns: ", df.columns)

"""##6 Select Specific Columns"""

df2=df.select(*["Bank Name", "City"])
df2.show()

"""##7 Select Multiple Columns"""

col_l=list(set(df.columns) - {"CERT", "ST"})
df2 = df.select(*col_l)
df2.show()

"""##8 Rename Column"""

df2 = df \
  .withColumnRenamed("Bank Name", "bank_name") \
  .withColumnRenamed("Acquiring Institution", "acq_institution") \
  .withColumnRenamed("Closing Date", "closing_date") \
  .withColumnRenamed("ST", "state") \
  .withColumnRenamed("CERT", "cert")

df2.show()

"""##9 Add Columns"""

df2=df.withColumn("state", col("ST"))
df2.show()

"""##10 Add Constant Column"""

df2 = df.withColumn("country", lit("US"))
df2.show()

"""##11 Drop Column"""

df2 = df.drop("CERT")
df2.show()

"""##12 Drop Multiple Column"""

df2 = df.drop(*["CERT", "ST"])
df2.show()

#modelo diferente
df2 = reduce(DataFrame.drop, ["CERT", "ST"], df)
df2.show()

"""##13 Filter Data"""

#Equals do Values
df2 = df.where(df["ST"]=="NE")
df2.show()

#Between values
df3=df.where(df["CERT"].between("1000", "2000"))
df3.show()

df4 = df.where(df["ST"].isin("NE", "IL"))
df4.show()

#contagem de cada filtro
df2 = df.where(df["ST"]=="NE")

df3=df.where(df["CERT"].between("1000", "2000"))

df4 = df.where(df["ST"].isin("NE", "IL"))

print("df.count: ", df.count())
print("df2.count: ", df2.count())
print("df3.count: ", df3.count())
print("df4.count: ", df4.count())

"""##14 Filter Data Using Logical Operator"""

df2 = df.where((df["ST"]=="NE")&(df["CITY"]=="Ericson"))
df2.show()

"""## 15 Replace Values in DataFrame"""

# Pre Replace
df.show()

# Post Replace
print("replace 7 in the above dataframe with 17 at all instances")
df.na.replace(7,17).show()

