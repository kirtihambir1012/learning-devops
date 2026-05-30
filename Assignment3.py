# from flask import Flask, jsonify
# import json

# app = Flask(__name__)

# @app.route('/api')
# def api():
#     file = open("data.json", "r")
#     data = json.load(file)
#     file.close()

#     return data

# app.run()



from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client.test
collection = db["students"]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        data = {
            "name": name,
            "email": email
        }

        collection.insert_one(data)

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)