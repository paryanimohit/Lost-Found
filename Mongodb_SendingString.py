from pymongo import MongoClient
import base64
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
with open("/home/krypton/Documents/Cam101_03_2019_16_03_33_448477.png", "rb") as imageFile:
    string = base64.b64encode(imageFile.read())
try:
    conn = MongoClient("mongodb+srv://admin:root1234@cluster0-3eho0.mongodb.net/test?retryWrites=true")
    print("Connected Successfully")
except:   
    print("Could not connect to MongoDB")
db=conn.MajorDatabase
collection = db.ImageDB
entry1 = { 
        "string":string
        } 
id1 = collection.insert_one(entry1)

print("Data inserted with record ids",id1)