from flask import Flask, request


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def connect():
    return "연결성공"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)