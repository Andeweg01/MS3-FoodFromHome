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



@app.route('/add_product')
def add_product():
    return render_template("addproduct.html", categories=mongo.db.categories.find())


@app.route('/insert_product', methods=['POST'])
def insert_product():
    products = mongo.db.products
    products.insert_one(request.form.to_dict())
    return redirect(url_for('get_products'))


@app.route('/edit_product/<product_id>')
def edit_product(product_id):
    the_product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editproduct.html', 
        product=the_product, categories=all_categories)


@app.route('/update_product/<product_id>', methods=['POST'])
def update_product(product_id):
    products = mongo.db.products
    products.update( {'_id': ObjectId(product_id)},
    {
        'product_name': request.form.get('product_name'),
        'product_brand': request.form.get('product_name'),
        'category_name': request.form.get('category_name'),
        'product_date': request.form.get('product_date'),
        'product_description': request.form.get('product_description'),
        'product_img': request.form.get('product_img'),
        'product_price': request.form.get('product_price'),
    })
    return redirect(url_for('get_products'))


@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    mongo.db.products.remove({'_id': ObjectId(product_id)})
    return redirect(url_for('get_products'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.categories.find())


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


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
    categories = mongo.db.categories
    category_doc = {'category_name': request.form.get('category_name')}
    categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0:8080'),
        port=int(os.environ.get('PORT', '5000')),
        debug=True)