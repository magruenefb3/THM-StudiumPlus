#import pymongo
import os
import pandas as pd
from pymongo import MongoClient

print(os.getcwd())
client = MongoClient ('localhost')
db = client["jsakila"]
collection = db["cinematicket"] 

# Load csv dataset
data = pd.read_csv('../Data/hans.csv')
print(data)


# Connect to MongoDB
data.reset_index(inplace=True)
data_dict = data.to_dict("records")
# Insert collection
collection.insert_many(data_dict)
