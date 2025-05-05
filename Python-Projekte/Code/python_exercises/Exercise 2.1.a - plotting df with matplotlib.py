"""
version 2023

@author: Grüne
based on examples in Dale, Kyran: Data Visualization with Python and JavaScript, O'Reilly

"""

import sqlalchemy
import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:hallo1234@localhost/sakila')
#df = pd.read_sql('actor', engine)
dbConnection = engine.connect()

df = pd.read_sql_query(
'''
select count(*) as rentals, DATE_FORMAT(rental_date, "%d-%m-%Y") as 'date' from rental
group by DATE_FORMAT(rental_date, "%d-%m-%Y");
''', dbConnection)

#pd.set_option('display.expand_frame_repr', False)
print(df)

dbConnection.close()

df.plot.bar()
plt.show()

"""


ax = df.plot.bar(x='date', y='rentals', rot=0)

def thin_xticks(ax, tick_gap=10, rotation=45):
    ticks = ax.xaxis.get_tickslocs()
    ticklabels = [l.get_text()\
                  for l in ax.xaxis.get_ticklabels()]
    ax.xaxis.set_ticks(ticks[::tick_gap])
    ax.xaxis.set_ticketlabels(ticklabels[::tick_gap],\
                              rotation=rotation)
    ax.figure.show()

#thin_xticks(ax)
"""