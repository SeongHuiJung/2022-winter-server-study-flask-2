from flask import Flask, request
from database.database import Database

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def connect():
    database=Database()

    id=request.args.get('id')
    password=request.args.get('password')

    row=database.execute_one("SELECT * FROM SeongHui.user WHERE id = '%s' AND pw = '%s';" %(id,password))
    database.commit()

    #아이디 비밀번호 일치
    if(row is not None):
        result="1"
        return result
    else:
        return "0"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)