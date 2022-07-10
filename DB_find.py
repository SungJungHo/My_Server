from pickle import NONE
from pymongo import MongoClient           # pymongo 임포트
from datetime import *
import time

def Find_Data(User_Name,AccountBalance):
    client = MongoClient("mongodb+srv://Cafe:Cafe@cluster1.btsz9.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    
    user = db.users.find_one({'name':User_Name})
    bal = Find_AccountBalance(User_Name)
    print(bal)
    if user == None:
        return "2"
    else :
        if not user["OnOff"]:
            return "3"
        else :
            if float(AccountBalance) == bal or bal < 0:
                return "1"
            else :
                return "4"

def Make_Log(User_Name,AccountBalance):
    client = MongoClient("mongodb+srv://Cafe:Cafe@cluster1.btsz9.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    Days = date.today().isoformat()
    t = time.strftime("%H:%M:%S",time.localtime())
    db.Logs.insert_one({'name':User_Name,"Day":Days,"Time":t,"AccountBalance":float(AccountBalance)})

def Find_AccountBalance(User_Name):
    client = MongoClient("mongodb+srv://Cafe:Cafe@cluster1.btsz9.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    deposit = db.Deposit.find_one({'name':User_Name})
    deposits = db.Deposit.find({'name':User_Name})
    user = db.Logs.find_one({'name':User_Name})
    users = db.Logs.find({'name':User_Name})
    text_List = []
    deposit_List = []
    deposits_Account = 0
    # print(user)
    
    if user == None:
        return -1
    else:
        for i in users:
            text_List.append([i["name"],i["Day"], i["Time"],i["AccountBalance"]])
        if deposit != None:
            Days = date.today().isoformat()
            for i in deposits:
                if i["Day"] == Days:
                    deposit_List.append(i["Deposit"])
            if len(deposit_List) > 0:
                for i in deposit_List:
                    deposits_Account = deposits_Account + i
                print(deposits_Account)
        AccountBalance = text_List[len(text_List)-1][3] + deposits_Account
        return AccountBalance

if __name__ == "__main__":
    # Find_Data("48093112")
    # Make_Data("nonottlyy")
    # Make_Log("nonottlyy",6666)
    print(Find_AccountBalance("48093112"))
    # print("gg")

