from flask import Flask,request
from DB_find import *
from datetime import *

app = Flask(__name__)

@app.route('/')
def mach_UserName():

    temp = request.args.get('name', "")
    check_User = Find_Data(temp)

    return check_User

@app.route('/Log')
def Call_Log():

    AccountName = request.args.get('name', "")
    AccountBalance = request.args.get('balance', "")
    Make_Log(AccountName,AccountBalance)
    return "sds"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
    