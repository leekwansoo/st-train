from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("URI")

#client = MongoClient("URI")
client = MongoClient("mongodb+srv://admin:james@cluster0.ujzjm.mongodb.net/todoapp?retryWrites=true&w=majority")
# database and collection code goes here
db = client.todoapp
coll = db.trains
# find code goes here
# iterate code goes here
# Close the connection to MongoDB when you're done.
#client.close()