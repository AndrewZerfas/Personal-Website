from flask import render_template
from flask_app import app

@app.route('/')
def home():
    return render_template('dashboard.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/links')
def links():
    return render_template('links.html')