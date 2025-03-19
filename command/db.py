import pymongo
from pymongo import MongoClient
from datetime import datetime


# Kết nối MongoDB
dbconnect = MongoClient("mongodb://localhost:27017/")
taskdb = dbconnect["taskdb"]
dailytask = taskdb["dailytask"]
oneTimeTask = taskdb["oneTimeTask"]
guild = taskdb["discord_server_list"]

# Hàm thêm task
def addDailyTasks(task):
    print("Adding task..." + task.__str__())
    dailytask.insert_one(task.to_dict())
    print("Task added successfully!")

def getDailyTask(guildid,dotw,time):
    tasks = dailytask.find({"guildid":guildid,"dotw":dotw,"time":time})
    dailytasks = list(tasks)
    return dailytasks

def getSpecificUserDailyTasks(guildid,userid):
    tasks_cursor = dailytask.find({"guildid":guildid,"userid": userid})
    tasks = list(tasks_cursor)  
    return tasks

def getSpecificUserOneTimeTasks(guildid,userid):
    tasks_cursor = oneTimeTask.find({"guildid":guildid,"userid": userid})
    tasks = list(tasks_cursor)  
    return tasks

def add_task(task):
    print("Adding task..." + task.__str__())
    oneTimeTask.insert_one(task.to_dict())
    print("Task added successfully!")

def getOneDayTask(guildid,time):
    tasks = oneTimeTask.find({"guildid":guildid,"time":time})
    return tasks

def deleteOneTimeTask(taskid):
    oneTimeTask.delete_one({"_id":taskid})
def updateOneTimeTask(taskid,new_time):
    oneTimeTask.update_one({"_id":taskid},{"$set":{"time":new_time}})

def setGuildidAndChannelID(guildid, channelid):
    existing_guild = guild.find_one({"guildid": guildid})  # Kiểm tra xem guild có tồn tại không
    if existing_guild:
        guild.update_one({"guildid": guildid}, {"$set": {"channelid": channelid}})
    else:
        guild.insert_one({"guildid": guildid, "channelid": channelid})

def getGuilddb():
    guilds = guild.find()
    list_guilds = list(guilds)
    return list_guilds

def deleteSpecificUserDailyTask(guildid,userid,taskname,dotw):
    dailytask.delete_one({"guildid":guildid,"userid":userid,"name":taskname,"dotw":dotw})

def deleteSpecificUserOneTimeTask(guildid,userid,taskname):
    oneTimeTask.delete_one({"guildid":guildid,"userid":userid,"name":taskname})

def deleteAllOneTimeTask():
    oneTimeTask.delete_many({})