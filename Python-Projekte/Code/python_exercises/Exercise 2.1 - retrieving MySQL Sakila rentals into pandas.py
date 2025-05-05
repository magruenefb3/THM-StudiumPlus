# install sqlalchemy with pip -- pip install sqlalchemy

import sqlalchemy

# install pandas  -- pip install pandas

import pandas as pd 

 # install mysql connector -- pip install mysql-connector-python

import mysql.connector

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root1234@localhost/sakila')

df = pd.read_sql_query("""select count(*) as rentals, 
                           DATE_FORMAT(rental_date, "%d-%m-%Y") as 'date' 
                            from rental group by DATE_FORMAT(rental_date, "%d.%m.%Y");""", 
                            engine)
print(df)