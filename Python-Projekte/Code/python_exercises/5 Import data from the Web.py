import requests
import pymongo
from pymongo import MongoClient

req = requests.get('https://zkillboard.com/api/losses/solo/')
req.raise_for_status()
recent_solo_losses_raw = req.json() #200 latest events

cluster = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
db = cluster["zkb"]
collection = db["one"] 

results = collection.insert_many(recent_solo_losses_raw)

print(recent_solo_losses_raw[0])