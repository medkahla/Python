from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/recipes/new')
def add_recipe():
    return render_template('add_recipes.html')


@app.route('/recipes/create', methods=["post"])
def create_recipe():
    if (Recipe.validate(request.form)):
        Recipe.create_rep(request.form)
        return redirect('/recipes')
    else:
        return redirect('/recipes/new')
    
@app.route('/recipes/<int:id>')
def recipeshow(id):
    recipe = Recipe.get_one(id)
    user = User.get_by_id({'id':session['user_id']})
    return render_template('recipe_show.html', recipe = recipe, user=user)

@app.route('/recipes/<int:id>/edit')
def recipeedit(id):
    recipe = Recipe.get_one(id)
    return render_template('recipe_edit.html', recipe = recipe)

@app.route('/recipes/<int:id>/update', methods=["post"])
def recipeupdate(id):
    print("updating ",id)
    Recipe.update(request.form)
    return redirect('/recipes')

@app.route('/recipes/<id>/destroy')
def destroy(id):
    Recipe.delete(id)
    return redirect('/recipes')