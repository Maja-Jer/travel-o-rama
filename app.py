import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Travel-O-Rama'
app.config["MONGO_URI"] = 'mongodb+srv://starting_point:Maja-page@cluster0-n1tx1.mongodb.net/Travel-O-Rama?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_trips')
def get_trips():
    return render_template("trips.html", 
    trips=mongo.db.trips.find())


@app.route('/add_trip')
def add_trip():
    return render_template('addtrip.html',
    categories=mongo.db.categories.find())


@app.route('/insert_trip', methods=['POST'])
def insert_trip():
    trips =  mongo.db.trips
    print(request.form)
    trips.insert_one(request.form.to_dict())
    return redirect(url_for('get_trips'))


@app.route('/edit_trip/<trip_id>')
def edit_trip(trip_id):
    the_trip =  mongo.db.trips.find_one({"_id": ObjectId(trip_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edittrip.html', trip=the_trip,
                           categories=all_categories)


@app.route('/update_trip/<trip_id>', methods=["POST"])
def update_trip(trip_id):
    trips = mongo.db.trips
    trips.update( {'_id': ObjectId(trip_id)},
    {
        'trip_location': request.form.get('trip_location'),
        'transport_code': request.form.get('transport_code'),
        'check_in': request.form.get('check_in'),
        'check_out': request.form.get('check_out'),
        'is_now': request.form.get('is_now'),
        'sights': request.form.get('sights'),
        'restaurants': request.form.get('restaurants'),
        'activities': request.form.get('activities')
    })
    return redirect(url_for('get_trips'))


@app.route('/delete_trip/<trip_id>')
def delete_trip(trip_id):
    mongo.db.trips.remove({'_id': ObjectId(trip_id)})
    return redirect(url_for('get_trips'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.categories.find())

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one(
    {'_id': ObjectId(category_id)}))

@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))

@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=os.environ.get('PORT', '5000'),
            debug=True)
