from flask import Flask
import pymysql


app = Flask(__name__)
db = pymysql.connect("localhost", "root", "", "db_demo2")
# app.config.from_object('config.py')
cursor = db.cursor()
@app.route('/')
def hello_world():

    cursor = db.cursor()
    return 'Hello World!'

@app.route('/show')
def show():

    return 'fdsf'
if __name__ == '__main__':
    app.run()
