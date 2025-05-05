"""
version 2023

@author: Grüne
based on examples in Dale, Kyran: Data Visualization with Python and JavaScript, O'Reilly
"""
import sqlalchemy
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:hallo1234@localhost/sakila')
dbConnection = engine.connect()

df = pd.read_sql_query(
'''
select count(*) as rentals, DATE_FORMAT(rental_date, "%d-%m-%Y") as 
'date' from rental
group by DATE_FORMAT(rental_date, "%d-%m-%Y");
''', dbConnection)

dbConnection.close()

ax = df.plot.bar(x='date', y='rentals', rot=0)
ax.set_xlabel("Date")
ax.xaxis.set_major_locator(plt.MaxNLocator(6))
ax.set_ylabel("Rentals")
plt.show() # only needed for PyCharm

