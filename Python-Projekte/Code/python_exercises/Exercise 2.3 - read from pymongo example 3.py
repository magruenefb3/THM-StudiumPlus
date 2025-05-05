import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
db = cluster["movies"]
collection = db["cinematicket"] 

results = collection.find({"film":"frozen1"})

for i in results:
    print(i["film"])
