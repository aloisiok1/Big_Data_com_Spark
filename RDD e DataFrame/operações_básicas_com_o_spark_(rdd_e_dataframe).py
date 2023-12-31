# -*- coding: utf-8 -*-
"""Operações Básicas com o Spark (RDD e DataFrame)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pMbnTC9_vdMtXcfd24t_5B6-8s6ggKc_

##1 Configurtação de Bibliotecas
"""

!pip install pyspark

from pyspark import SparkContext
from pyspark.sql import SparkSession

sc=SparkContext.getOrCreate()

spark=SparkSession.builder.appName("PySpark DataFrame From Rdd").getOrCreate()

"""##2 Create PySpark DataFrame from ans Existing RDD"""

rdd = sc.parallelize([("C", 85, 76, 87, 91), ("B", 85, 76, 87, 91), ("A", 85, 78, 96, 92), ("A", 92, 76, 89, 96)], 4)

print(type(rdd))

sub = ["id_person", "value_1", "value_2", "value_3", "value_4"]

marks_df = spark.createDataFrame(rdd, schema=sub)

print(type(marks_df))

marks_df.printSchema()

marks_df.show()

"""##3 Creation e Manipulation in PySpark DataFrame"""

!pip install pyspark
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("pysparkdf").getOrCreate()

"""##4 Importing Data"""

df = spark.read.csv("/content/cereal.csv", sep = ",", inferSchema = True, header = True)

"""##5 Reading de Schema"""

df.printSchema()

"""##6 Select()"""

df.select("name", "mfr", "rating").show()

"""##7 withColumn() Mudança de Nome e função com o Cast"""

df.withColumn("Calories", df["calories"].cast("String")).printSchema()

"""##8 groupBy"""

df.groupBy("name", "calories").count().show()

df.groupBy("calories").count().show()

"""##9 orderBy()"""

#ordenando pela coluna protein
df.orderBy("protein").show()

#ordenando pela coluna calories
df.orderBy("calories").show()

"""##10 Case When"""

from pyspark.sql.functions import when

df.select("name", when(df.vitamins >= "25", "rich in vitamins")).show()

"""##11 filter()"""

df.filter(df.calories=="100").show(50)

"""##12 isNull() / isNotNull()"""

# (*) no final vai baicar toda a biclioteca
from pyspark.sql.functions import *

#trouxe todas as linhas que não são nulas
df.filter(df.name.isNotNull()).show()

#trouxe todas as linhas que são nulas
df.filter(df.name.isNull()).show()

#trouxe todas as linhas que são nulas na contagem
df.filter(df.name.isNull()).count()

#trouxe todas as linhas que não são nulas na contagem
df.filter(df.name.isNotNull()).count()

"""##13 exemplos práticos de Transformações"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder     .appName("Exemplos PySpark")     .getOrCreate()


# Carregar dados de um arquivo CSV
df = spark.read.csv("/content/cereal.csv", header=True, inferSchema=True)

# Exibir o schema do DataFrame
df.printSchema()

# Selecionar colunas específicas
df_selected = df.select("mfr", "type")

# Filtrar registros com base em uma condição
df_filtered = df.filter(col("calories") > 100)

# Adicionar uma nova coluna calculada
df_with_new_column = df.withColumn("nova_coluna", col("fat") * 2)

# Renomear uma coluna
df_renamed_column = df_with_new_column.withColumnRenamed("nova_coluna", "double_fat")

df_selected.printSchema()

df_filtered.show()

df_with_new_column.printSchema()

df_renamed_column.printSchema()

"""##14 Exemplos práticos de Ações"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder     .appName("Exemplos PySpark")     .getOrCreate()

# Carregar dados de um arquivo CSV
df = spark.read.csv("/content/cereal.csv", header=True, inferSchema=True)

# Contar o número total de registros
count = df.count()
print("Número total de registros: ", count)

# Exibir uma amostra dos dados
df_sample = df.sample(fraction=0.1, seed=42)
df_sample.show()

# Calcular a média de uma coluna
average = df.select("calories").groupBy().avg().collect()[0][0]
print("Média das calorias: ", average)

# Salvar o DataFrame em um arquivo CSV
df.write.csv("/arquivo_teste.csv", header=True)

df1 = spark.read.csv("/arquivo_teste.csv", sep = ",", inferSchema = True, header = True)
df1.show()

