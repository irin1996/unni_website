from flask import Blueprint, render_template
import json

services = Blueprint("services", __name__)  # Create a Blueprint named 'services'

@services.route("/services")
def services_list():
    with open("static/products.json", "r") as f:
        products = json.load(f)
    
    current_page = {"name": "商品一覧", "url": "/services"}
    return render_template("services.html", products=products, current_page=current_page)