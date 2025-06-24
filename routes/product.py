from flask import Blueprint, render_template, abort
import json

product = Blueprint("product", __name__)  # Create a Blueprint named 'product'

@product.route("/product/<int:product_id>")
def product_detail(product_id):
    # Load product data from JSON file
    with open("static/products.json", "r") as f:
        products = json.load(f)

    # Find the product with the matching ID
    product_data = next((product for product in products if product["id"] == product_id), None)

    # If product not found, return a 404 error
    if not product_data:
        abort(404)

    # Render the product.html template with the product data
    return render_template("product.html", product=product_data)