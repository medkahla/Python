from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def direct():
    return redirect('/dojos')

@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create():
    Dojo.add_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/show/<int:dojo_id>')
def dojo_show(dojo_id):
    dojo = Dojo.get_one(dojo_id)
    ninjas = Ninja.get_list(dojo_id)
    return render_template("dojo_show.html",dojo=dojo, ninjas=ninjas)