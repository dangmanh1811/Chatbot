from pymongo.mongo_client import MongoClient

import os
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv('MONGODB_URI')

#  Create a new client and connect to the server
client = MongoClient(uri)
db = client['user_db']
users_collection = db['users']
