from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.party import Party
from flask_app.models.user import User

@app.route('/parties/new')
def add_party():
    return render_template('new_party.html')

@app.route('/parties/create', methods=["post"])
def create():
    if (Party.validate(request.form)):
        data = {
            **request.form,
            'user_id':session['user_id']
        }
        Party.create_party(data)
        return redirect('/dashboard')
    return redirect('/parties/new')