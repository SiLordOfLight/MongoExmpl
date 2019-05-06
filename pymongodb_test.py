from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask_oauthlib.client import OAuth
from flask import render_template, flash
import pymongo

import pprint
import os
import json
import datetime as dt
app = Flask(__name__)

app.debug = True #Change this to False for production

app.secret_key = os.environ['SECRET_KEY'] #used to sign session cookies
oauth = OAuth(app)
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

url = 'mongodb://{}:{}@{}/{}'.format(
    os.environ["MONGO_USERNAME"],
    os.environ["MONGO_PASSWORD"],
    os.environ["MONGO_HOST"],
    os.environ["MONGO_DBNAME"])

client = pymongo.MongoClient(os.environ["MONGO_HOST"])
db = client[os.environ["MONGO_DBNAME"]]

@app.route("/")
def main():
    #1. print the number of documents in collection
    print(len(collection.find()))
    #2. print the first document in the collection
    print(collection.findone())
    #3. print all documents in the collection
    print(collection.find())
    #4. print all documents with a particular value for some attribute
    print(collection.find({"sender":"SiLordOfLight"}))


if __name__=="__main__":
    app.run()