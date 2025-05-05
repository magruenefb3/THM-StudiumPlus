#import pymongo
import pandas as pd
from pymongo import MongoClient

client = MongoClient ('localhost')
db = client["movies"]
collection = db["cinematicket"] 

cursor = collection.find() # load all entries into the iterator 'cursor'
entries = list(cursor)     # we do now create a list
df =pd.DataFrame(entries)  # now we create a DataFrame from the list

print(df.head())
#print(df)