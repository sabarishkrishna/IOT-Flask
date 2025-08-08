from pymongo.mongo_client import MongoClient
import certifi

uri = "mongodb+srv://sabarishkrishna71:Password123@iotcloud.speaadk.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())

db = client.iotcloud

result = db.users.find_one({"username": "sabarish"})

print(result)