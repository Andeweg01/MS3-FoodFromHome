import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path 
if path.exists("env.py"): 
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'ffh'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_products')
def get_products():
    return render_template("products.html", products=mongo.db.products.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0:8080'),
        port=int(os.environ.get('PORT', '5000')),
        debug=True)