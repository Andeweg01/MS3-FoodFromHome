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

# The first route getting all the products on screen

@app.route('/')
@app.route('/get_products')
def get_products():
    category = mongo.db.categories.find()
    country = mongo.db.origin.find()
    products = mongo.db.product.find()

    return render_template("products.html",
                            products=products,
                            categories=category,
                            origin=country)


# The filtering route filtering on category_name and origin_name
# returning either a render_template for filteredproducts.html
# or products.html when nothing is selected

@app.route('/get_filtered', methods=["GET", "POST"])
def get_filtered():
    category = mongo.db.categories.find()
    country = mongo.db.origin.find()
    products = mongo.db.product.find()
    filters = {}

    if request.method == "POST":
        product_category = request.form.get("category_name")
        if product_category:
            filters["category_name"] = product_category
            filtered_results = mongo.db.product.find(filters)

        product_origin = request.form.get("country_name")
        if product_origin:
            filters["origin_name"] = product_origin
            filtered_results = mongo.db.product.find(filters)
        return render_template("filteredproducts.html",
                               products=filtered_results,
                               categories=category,
                               origin=country)
    else:
        return render_template("products.html",
                               products=mongo.db.product.find())


# When clicked renders the opening page for editing products
@app.route('/edit_products')
def edit_products():
    return render_template("editproducts.html",
    products=mongo.db.product.find())


# When clicked renders the opening page for adding products
@app.route('/add_product')
def add_product():
    return render_template("addproduct.html",
    categories=mongo.db.categories.find())


# Inserts the data to the product collection and redirects
# to the page to add a supplier for the product to the supplier collection
@app.route('/insert_product', methods=['POST'])
def insert_product():
    product = mongo.db.product
    product.insert_one(request.form.to_dict())
    return render_template("addsupplier.html")


# Inserts the supplier to the supplier collection
@app.route('/insert_supplier', methods=['POST'])
def insert_supplier():
    supplier = mongo.db.supplier
    supplier.insert_one(request.form.to_dict())
    return redirect(url_for('get_products'))


# When clicked render editproduct.html where the edits can be made
@app.route('/edit_product/<product_id>')
def edit_product(product_id):
    the_product = mongo.db.product.find_one({"_id": ObjectId(product_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editproduct.html',
        product=the_product, categories=all_categories)


# To update the product with data from the form in editproduct.html
@app.route('/update_product/<product_id>', methods=['POST'])
def update_product(product_id):
    products = mongo.db.product
    products.update({'_id': ObjectId(product_id)},
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


# When clicked deletes the selected product
@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    mongo.db.product.remove({'_id': ObjectId(product_id)})
    return redirect(url_for('get_products'))


# Showing the available categories
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.categories.find())


# When clicked renders the editcategory.html page where changes can be made
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


# Updates the category with the data entered on editcategory.html
@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


# When clicked deletes the selected category
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


# Inserts the new category givin in addcategory.html
@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    category_doc = {'category_name': request.form.get('category_name')}
    categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


# Renders the addcategory.html page
@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


# Renders the about.html page
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0:8080'),
        port=int(os.environ.get('PORT', '5000')),
        debug=True)
