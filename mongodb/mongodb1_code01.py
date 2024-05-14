from pymongo import MongoClient


client = MongoClient

db = client.myfirstmongodb  # myfirstmongodb = database name
collection = db.myfirstcollection  # myfirstcollection = collection name

client.close()
