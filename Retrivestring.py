from Connection import MongoConnection
collect=MongoConnection.getConnection()
print(collect.find_one())
