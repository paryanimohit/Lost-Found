import base64
import os
from Connection import MongoConnection
class UploadImage():
    def upload(self):
        j=0
        collect=MongoConnection.getConnection()
        listImages=os.listdir("/home/krypton/Documents/Image")
        
        for i in listImages:
            with open("/home/krypton/Documents/Image/"+i, "rb") as imageFile:
                string = base64.b64encode(imageFile.read())
                dataDict={"Image"+str(j):
                            string
                       }
                collect.insert_one(dataDict)
                j=j+1
                os.remove("/home/krypton/Documents/Image/"+i)
        print("Data inserted with record ids")
    
obj = UploadImage()
obj.upload()
