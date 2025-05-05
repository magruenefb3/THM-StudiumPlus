# install sqlalchemy with pip -- pip install sqlalchemy

import sqlalchemy

# install pandas  -- pip install pandas

import pandas as pd 

 # install mysql connector -- pip install mysql-connector-python

import mysql.connector

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:hallo1234@localhost/sakila')

df = pd.read_sql('actor', engine)
print(df.head())