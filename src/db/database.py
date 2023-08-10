from pymongo import MongoClient
import os

client = MongoClient(os.environ["MONGO_URI"])
db = client[os.environ["DATABASE_NAME"]]
collection = db[os.environ["COLLECTION_NAME"]]
