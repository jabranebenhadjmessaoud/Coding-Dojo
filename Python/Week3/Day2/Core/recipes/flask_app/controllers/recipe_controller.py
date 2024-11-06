from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User
from flask import render_template, redirect, request, session,flash
from flask_app import app


@app.route('/recipes/new')
def create_recipe():
    if not 'user_id' in session :
        return redirect('/')
    return render_template('new_recipe.html')


@app.route('/recipes/create',methods=["post"])
def add_recipe():
    
    if Recipe.validate_recipe(request.form) :
        data={
            **request.form ,
            "user_id":session['user_id']
        }
        print("***"*20)
        print("this is after recipe validation and before creating")
        recipe_id=Recipe.add_recipe(data)
        print("***"*20)
        print("this is after creating the add recipe ")
        return redirect('/dashboard')
    
@app.route('/dashboard')
def show_all():
    if not 'user_id' in session :
        return redirect('/')
    recipes=Recipe.get_all()
    print("after get all in controller")
    logged_user=User.get_by_id({'id':session['user_id']})
    return render_template('recipes.html',recipes=recipes,user=logged_user) 

@app.route('/recipes/<int:id>')
def show_one(id):
    if not 'user_id' in session :
        return redirect('/')
    recipe=Recipe.get_by_id({'id':id})
    logged_user=User.get_by_id({'id':session['user_id']})
    return render_template('show_one_recipe.html',recipe=recipe,user=logged_user)


@app.route('/recipes/<int:id>/delete',methods=["post"])
def delete(id):
    Recipe.delete({'id':id})
    return redirect("/dashboard")


@app.route('/recipes/<int:id>/edit')
def edit(id):
    if not 'user_id' in session :
        return redirect('/')
    recipe=Recipe.get_by_id({'id':id})
    return render_template("edit_recipe.html",recipe=recipe)



@app.route('/recipes/<int:id>/update',methods=["post"])
def update(id):
    if Recipe.validate_recipe(request.form):
        data={
            **request.form,
            "id":id
        }
        Recipe.update(data)
        return redirect('/dashboard')
    return redirect(f'/recipes/{id}/edit')   