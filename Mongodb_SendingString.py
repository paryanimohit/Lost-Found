from pymongo import MongoClient
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
try:
    conn = MongoClient("mongodb+srv://admin:root1234@cluster0-3eho0.mongodb.net/test?retryWrites=true")
    print("Connected Successfully")
except:   
    print("Could not connect to MongoDB")
db=conn.MajorDatabase
collection = db.ImageDB
entry1 = { 
        "string":"hello"
        } 
id1 = collection.insert_one(entry1)

print("Data inserted with record ids",id1)