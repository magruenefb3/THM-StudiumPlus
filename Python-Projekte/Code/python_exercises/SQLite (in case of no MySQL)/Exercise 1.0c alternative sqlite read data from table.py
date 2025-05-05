""" Sample taken from
    https://towardsdatascience.com/yes-python-has-a-built-in-database-heres-how-to-use-it-b3c033f172d3
    
    date 11-06-2023
 """
 
import sqlite3

# create a connection
conn = sqlite3.connect('students.db')

# create a table
c = conn.cursor()  # cursor

c.execute("SELECT * FROM students")
print(c.fetchall())

# commit
conn.commit()

# close the connection
conn.close()