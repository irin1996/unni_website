from flask import Blueprint, render_template

profile = Blueprint("profile", __name__)  # Create a Blueprint named 'profile'

@profile.route("/profile")
def profile_page():
    current_page = {"name": "会社案内", "url": "/profile"}
    return render_template("profile.html", current_page=current_page)