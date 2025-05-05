""" attention, running this might fail in VSCode.
    This is due to PowerShell. 

"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('students.db')
df = pd.read_sql_query("SELECT * FROM students;", conn)
print(df)
conn.commit()
conn.close()