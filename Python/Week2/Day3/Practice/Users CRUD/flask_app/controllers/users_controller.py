from flask import session, request, render_template, redirect
from flask_app.models.user_model import User
from flask_app import app


@app.route("/users/new")
def create_user():
    print ("8"*100)
    return render_template("create.html")
@app.route("/users/create",methods=["POST"])
def created():
    new_user={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }

    # list_of_users.append(new_user)
    result=User.create(new_user)
    return redirect("/users")


@app.route("/users")
def read_all():
    list_of_users1=User.get_all()
    return render_template("readall.html",list_of_users=list_of_users1)

@app.route("/users/delete/<int:id>",methods=["post"])
def delete_one(id):
    data ={
        "id":id
    }
    User.delete_one(data)
    redirect("/users")



@app.route("/users/<int:user_id>")
def show():
    usertoshow=User.show_one()
    return render_template("readone.html",usertoshow=usertoshow)
