import string
from pymongo import MongoClient           # pymongo 임포트
from datetime import *
import time
def Make_Data(User_Name):
    client = MongoClient("mongodb+srv://Cafe:Cafe@cluster1.btsz9.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    db.users.insert_one({'name':User_Name})

def Find_Data(User_Name):
    client = MongoClient("mongodb+srv://Cafe:Cafe@cluster1.btsz9.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    
    user = db.users.find_one({'name':User_Name})
    if user == None:
        return "no"
    else :
        return "yes"

def Make_Log(User_Name,AccountBalance):
    client = MongoClient("mongodb+srv://Cafe:Cafe@cluster1.btsz9.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    Days = date.today().isoformat()
    t = time.strftime("%H:%M:%S",time.localtime())
    db.Logs.insert_one({'name':User_Name,"Day":Days,"Time":t,"AccountBalance":AccountBalance})

if __name__ == "__main__":
    # Make_Data("nonottlyy")
    print(Find_Data("nonottlyy"))
    Make_Log("nonottlyy",6666)

