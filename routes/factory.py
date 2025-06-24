from flask import Blueprint, render_template

factory = Blueprint("factory", __name__)  # Create a Blueprint named 'factory'

@factory.route("/factory")
def factory_page():
    current_page = {"name": "工場概要", "url": "/factory"}
    return render_template("factory.html", current_page=current_page)