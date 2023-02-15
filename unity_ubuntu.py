from flask import Flask, request
from database.database import Database

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def connect():
    database=Database()
    row=database.execute_one("SELECT * FROM SeongHui.user WHERE id = '%s' AND pw = '%s';" %("9","9"))
    #id=request.args.get('id')
    if(row is not None):
        return database
    #return "연결성공"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)