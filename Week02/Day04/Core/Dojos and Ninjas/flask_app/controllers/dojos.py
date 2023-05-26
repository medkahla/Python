from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create():
    Dojo.add_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<id>')
def liste(id):
    dojo = Dojo.get_one(id)
    ninjas = Ninja.get_list(dojo)
    return render_template("list_ninjas.html", ninjas = ninjas, dojo=dojo)