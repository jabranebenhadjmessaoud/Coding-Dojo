from flask import render_template,request,redirect,flash
from flask_app import app
from flask_app.models.email_model import Email

@app.route('/')
def home_page():
    print ('inside the route')
    list_of_emails1=Email.get_all()
    print("inside home page route")
    return render_template("index.html",list_of_emails=list_of_emails1)

@app.route("/delete/<int:id>",methods=["post"])
def delete_one(id):
    data ={
        "id":id
    }
    Email.delete_one(data)
    return redirect("/")



@app.route('/create', methods=["post"])
def create_new():
    data={
        **request.form
    }
    print (data)
    if not Email.validate_email(request.form):
        # flash("Email cannot be blank!", 'email_validation')
        print ("error ","@"*20)
        return redirect('/')
    else :
        result=Email.add_new(data)
        flash("Email added successfully","email_validation")
        print ("email saved ","@"*20)
        return redirect('/')