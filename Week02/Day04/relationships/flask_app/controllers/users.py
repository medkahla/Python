from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template("index.html", users = users)

@app.route('/users/create', methods=["POST"])
def create():
    User.create_user(request.form)
    return redirect('/')