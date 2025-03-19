import pymongo
from pymongo import MongoClient
from datetime import datetime


# Kết nối MongoDB
dbconnect = MongoClient("mongodb://localhost:27017/")
taskdb = dbconnect["taskdb"]
dailytask = taskdb["dailytask"]
oneTimeTask = taskdb["oneTimeTask"]

# Hàm thêm task
def addDailyTasks(task):
    print("Adding task..." + task.__str__())
    dailytask.insert_one(task.to_dict())
    print("Task added successfully!")

def getDailyTask(dotw,time):
    tasks = dailytask.find({"dotw":dotw,"time":time})
    dailytasks = list(tasks)
    return dailytasks

def getSpecificUserDailyTasks(userid):
    tasks_cursor = dailytask.find({"userid": userid})
    tasks = list(tasks_cursor)  
    return tasks

def add_task(task):
    print("Adding task..." + task.__str__())
    oneTimeTask.insert_one(task.to_dict())
    print("Task added successfully!")

def getOneDayTask(time):
    tasks = oneTimeTask.find({"time":time})
    return tasks

def deleteOneTimeTask(taskid):
    oneTimeTask.delete_one({"_id":taskid})
def updateOneTimeTask(taskid,new_time):
    oneTimeTask.update_one({"_id":taskid},{"$set":{"time":new_time}})