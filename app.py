import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path 
if path.exists("env.py"): 
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'ms3-ffh'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_products')
def get_products():
    return render_template("products.html", 
    products=mongo.db.product.find())


@app.route('/get_country')
def get_country():
    return render_template("products.html", 
    products=mongo.db.product.find())


@app.route('/edit_products')
def edit_products():
    return render_template("editproducts.html", 
    products=mongo.db.product.find())


@app.route('/add_product')
def add_product():
    return render_template("addproduct.html", 
    categories=mongo.db.categories.find())


@app.route('/insert_product', methods=['POST'])
def insert_product():
    product = mongo.db.product
    product.insert_one(request.form.to_dict())
    return render_template("addsupplier.html")


@app.route('/insert_supplier', methods=['POST'])
def insert_supplier():
    supplier = mongo.db.supplier
    supplier.insert_one(request.form.to_dict())
    return redirect(url_for('get_products'))


@app.route('/edit_product/<product_id>')
def edit_product(product_id):
    the_product = mongo.db.product.find_one({"_id": ObjectId(product_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editproduct.html', 
        product=the_product, categories=all_categories)


@app.route('/update_product/<product_id>', methods=['POST'])
def update_product(product_id):
    products = mongo.db.product
    products.update( {'_id': ObjectId(product_id)},
    {
        'category_name': request.form.get('category_name'),
        'product_name': request.form.get('product_name'),
        'product_brand': request.form.get('product_brand'),
        'product_description': request.form.get('product_description'),
        'product_price': request.form.get('product_price'),
        'entry_date': request.form.get('entry_date'),
        'origin_name': request.form.get('origin_name'),
        'supplier_name': request.form.get('supplier_name'),
        'user_code': request.form.get('user_code'),
    })
    return redirect(url_for('get_products'))


@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    mongo.db.product.remove({'_id': ObjectId(product_id)})
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