from datetime import datetime

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.test


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detail/<idx>')
def detail(idx):
    return render_template('detail.html')

@app.route('/post', methods=['POST'])
def save_post():
    title_receive = request.form["title_give"]
    password_receive = request.form["password_give"]
    content_receive = request.form["content_give"]

    doc = {
        'title': title_receive,
        'password': password_receive,
        'content': content_receive
    }
    db.test.insert_one(doc)

    return {"result": "success"}


@app.route('/post', methods=['GET'])
def get_post():
    posts = 0
    posts = list(db.test.find({},{'_id':False}))
    return jsonify({"posts": posts})


@app.route('/post', methods=['DELETE'])
def delete_post():
    idx = request.args.get('idx')
    db.test.delete_one({'idx': int(idx)})
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)