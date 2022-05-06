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
    # todo
		return

@app.route('/articleList', methods=['GET'])
def get_article_list():
    article_list = list(db.timeattck.find({}))
      #
	  # for article in article_list:
		#   article['reg_date'] = article['reg_date'].strftime('%Y.%m.%d %H:%M:%S')

    return jsonify({"article_list": article_list})

# Create
@app.route('/article', methods=['POST'])
def create_article():
    title_receive = request.form["title_give"]
    pw_receive = request.form["pw_give"]
    content_receive = request.form["content_give"]
    print(title_receive, pw_receive, content_receive)
    file = request.files["file_give"]

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename= f'file-{mytime}'

    doc = {
        'title': title_receive,
        'pw': pw_receive,
        'content': content_receive,
        'file':f'{filename}.{extension}'
    }

    db.timeattck.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '포스팅성공!'})

# Read
@app.route('/article', methods=['GET'])
def read_article():
    article = 0 #todo
    return jsonify({"article": article})

# Update
@app.route('/article', methods=['PUT'])
def update_article():
    db.timeattck.update_one
    return {"result": "success"}

# Delete
@app.route('/article', methods=['DELETE'])
def delete_article():
    db.timeattck.delete_one({'title':title})
    return {"result": "success"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
