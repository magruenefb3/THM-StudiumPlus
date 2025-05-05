""" Sample taken from
    https://towardsdatascience.com/yes-python-has-a-built-in-database-heres-how-to-use-it-b3c033f172d3
    
    date 11-06-2023
 """
 
import sqlite3

# create a connection
conn = sqlite3.connect('students.db')

# create a table
c = conn.cursor()  # cursor

all_students = [
    ('john', 21, 1.8),
    ('david', 35, 1.7),
    ('michael', 19, 1.83),
]
c.executemany("INSERT INTO students VALUES (?, ?, ?)", all_students)

# commit
conn.commit()

# close the connection
conn.close()