from flask import Flask ,jsonify,render_template,url_for,redirect,abort, request
from flask_sqlalchemy import *

app = Flask('kkk')
@app.route('/hello', methods=['GET', 'POST'])
def test1():
    return "test.html"


app.run()

