from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja

from flask_app.models.dojo import Dojo

@app.route('/ninjas/new')
def new_ninja():
    dojos = Dojo.get_all()
    ninjas = Ninja.get_all()
    return render_template("ninjas.html", dojos=dojos, ninjas=ninjas)

@app.route('/ninjas/create', methods=['POST'])
def add_ninja():
    Ninja.add_ninja(request.form)
    return redirect('/dojos')