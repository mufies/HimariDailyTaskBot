import pymongo
from pymongo import MongoClient
from datetime import datetime


# Kết nối MongoDB
dbconnect = MongoClient("mongodb://localhost:27017/")
taskdb = dbconnect["taskdb"]
collection = taskdb["tasks"]

# Hàm thêm task
def add_task(task):
    print("Adding task..." + task.__str__())
    collection.insert_one(task.to_dict())
    print("Task added successfully!")

def get_tasks():
    tasks = collection.find()
    return tasks