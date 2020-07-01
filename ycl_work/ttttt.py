from flask import Flask, jsonify, render_template, url_for, redirect, abort, request


def readcard():
    with open("basic_wordcloud.html") as f:
        line = f.read()
        print(line)
        return line


app = Flask('kkk')
@app.route('/hello', methods=['GET', 'POST'])
def test1():
    return render_template("test.html", chinamap=readcard())


app.run()

