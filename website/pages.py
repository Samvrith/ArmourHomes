from flask import Blueprint, render_template

pages = Blueprint('pages', __name__)

@pages.route('/')
def home():
    return render_template("index.html")

@pages.route('/services')
def services():
    return render_template("services.html")

@pages.route('/about')
def about():
    return render_template("about.html")

@pages.route('/contact')
def contact():
    return render_template("contact.html")
