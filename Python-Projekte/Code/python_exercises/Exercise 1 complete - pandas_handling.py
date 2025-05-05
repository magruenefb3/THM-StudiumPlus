# code from:
# https://kb.objectrocket.com/mongo-db/how-to-import-and-export-mongodb-data-using-pandas-in-python-355

import pymongo
from pymongo import MongoClient
import pandas
import numpy as np

# build a new client instance of MongoClient
mongo_client = MongoClient('localhost', 27017)

# create new database and collection instance
db = mongo_client.pandas_database
col = db.pandas_collection


mongo_docs = [
    {"_id": "1111111", "field 1" : 'Object Rocket 1', "field 2" : 'Object Rocket 21'},
    {"_id": "2222222", "field 1" : 'Object Rocket 2', "field 2" : 'Object Rocket 22'},
    {"_id": "3333333", "field 1" : 'Object Rocket 3', "field 2" : 'Object Rocket 23'},
    {"_id": "4444444", "field 1" : 'Object Rocket 4', "field 2" : 'Object Rocket 24'}
]

# create an empty dictionary for the MongoDB documents' fields
fields = {}

# go through list of MongoDB documents
for doc in mongo_docs:

    # iterate key-value pairs of each MongoDB document
    # use iteritems() for Python 2
    for key, val in doc.items():

        # attempt to add field's value to dict
        try:
            # append the MongoDB field value to the NumPy object
            fields[key] = np.append(fields[key], val)
        except KeyError:
            # create a new dict key will new NP array
            fields[key] = np.array([val])

# print out the fields dictionary
print (fields)

# create an empty list for the Series objects
series_list = []

# iterate over the dict of lists
for key, val in fields.items():

    # convert the 'fields' NumPy arrays into Pandas Series
    if key != "_id":
        fields[key] = pandas.Series(fields[key])
        fields[key].index = fields["_id"]

        print ("\n\n-----------------------------")
        print (key)
        print (fields[key])
        print (fields[key].index)

        # put the series with index into a list
        series_list += [fields[key]]

# create a dictionary for the DataFrame frame dict
df_series = {}
for num, series in enumerate(series_list):
    # same as: df_series["data 1"] = series
    df_series['data ' + str(num)] = series

# create a DataFrame object from Series dictionary
mongo_df = pandas.DataFrame(df_series)
print ("\nmongo_df:", type(mongo_df))

# iterate over DataFrame object
for series in mongo_df.itertuples():
    for num, item in enumerate(series):
        print (item)
    print (series)
    print ("\n")