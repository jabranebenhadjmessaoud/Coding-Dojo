from flask import Flask,render_template,redirect,session,request 
from user_model import User
app=Flask(__name__)

# list_of_users=[
#     { 
#         "id":1,
#         "first_name":"foulen",
#         "last_name":"ben",
#         "email":"jabrane@mail.com",
#         "created_at":"18/04/2024"
#     },
#     {
#         "id":2,
#         "first_name":"jabrane",
#         "last_name":"ben",
#         "email":"jabrane@mail.com",
#         "created_at":"18/04/2024"
#     },
#     {
#         "id":3,
#         "first_name":"mohamed",
#         "last_name":"ben",
#         "email":"jabrane@mail.com",
#         "created_at":"18/04/2024"
#     }
# ]
# list_of_users=[]

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




if __name__=="__main__":
    app.run(debug=True)
