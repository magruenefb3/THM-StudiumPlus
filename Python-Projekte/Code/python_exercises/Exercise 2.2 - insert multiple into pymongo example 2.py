import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
db = cluster["movies"]
collection = db["cinematicket"] 
post1 = {"_id":5, "film":"Reservoir Dogs"}
post2 = {"_id":6, "film":"Pizza Lammbock"}

collection.insert_many([post1, post2])
