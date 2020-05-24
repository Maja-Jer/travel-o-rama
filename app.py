import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Travel-O-Rama'
app.config["MONGO_URI"] = 'mongodb+srv://starting_point:Maja-page@cluster0-n1tx1.mongodb.net/Travel-O-Rama?retryWrites=true&w=majority'

mongo = PyMongo(app)
for i in mongo.db.trip_type.find():
    print(i)

@app.route('/')
@app.route('/get_trips')
def get_trips():
    print(mongo.db.trip_type.find())
    return render_template("trips.html", trip_type=mongo.db.trip_type.find())



if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=os.environ.get('PORT', '5000'),
            debug=True)