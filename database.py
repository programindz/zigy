import pymongo
from gridfs import GridFS

#use mongodb to store videos and access them 
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["zigy_videos"]
fs = GridFS(db)