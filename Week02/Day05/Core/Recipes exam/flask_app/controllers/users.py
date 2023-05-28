from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)     # type: ignore # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users/create',methods=['POST'])
def create_user():
    print(request.form)
    if(User.validate(request.form)):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            **request.form,'password':pw_hash
        }
        user_id = User.create_user(data)
        session['user_id'] = user_id
        return redirect('/recipes')
    return redirect('/')

@app.route('/recipes')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    user = User.get_by_id({'id':session['user_id']})
    recipes = Recipe.get_link()
    return render_template("recipes.html", user = user, recipes=recipes)

@app.route('/users/login', methods=['POST'])
def login():
    user_from_db = User.get_by_email({'email':request.form['email']})
    if(user_from_db):
        # check password
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        # if we get False after checking the password
            flash("Invalid Password", "Login")
            return redirect('/')
        session['user_id'] = user_from_db.id
        return redirect('/recipes')
    flash("Invalid Email", "Login")
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')