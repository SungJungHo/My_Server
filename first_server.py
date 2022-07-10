from flask import Flask,request
from DB_find import *
from datetime import *
import threading, time

thread_Count = 0

app = Flask(__name__)

@app.route('/')
def mach_UserName():

    temp = request.args.get('name', "")
    AccountBalance = request.args.get('AccountBalance', "")
    check_User = Find_Data(temp,AccountBalance)

    return check_User

@app.route('/Log')
def Call_Log():

    AccountName = request.args.get('name', "")
    AccountBalance = request.args.get('balance', "")
    Make_Log(AccountName,AccountBalance)
    return "sds"


if __name__ == '__main__':
    # def getHtml():
        
    #     while True:
    #         time.sleep(5)
    #         print(date.today().isoformat())
    #         print(time.strftime("%H:%M:%S",time.localtime()))
            
    # threading.Thread(target=getHtml).start()
    app.run(debug=True,host='0.0.0.0', port=80)
    