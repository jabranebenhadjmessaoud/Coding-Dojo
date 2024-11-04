from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self,data):
        self.id=data['id']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def add_new(cls,data):
        query="insert into emails (email) values (%(email)s)"
        result=connectToMySQL(DB).query_db(query,data)
        print (result)    

    @staticmethod
    def validate_email( data ):
        is_valid = True
        mailtoadd=data["email"]
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!",'email_validation')
            print("invalid mail aa dadsadaazazdaz")
            is_valid = False
            ########################################
        for i in range (1,6):
            query="select email from emails where id=%(i)s"
            result=connectToMySQL(DB).query_db(query,data)
            print(result)
            print (mailtoadd)
            if (result==mailtoadd):
                flash("Email Already exist",'email_validation')
                is_valid = False
                break
            #############################################
        return is_valid 


    @classmethod
    def get_all(cls):
        query="select * from emails ;"
        result=connectToMySQL(DB).query_db(query)
        print("@"*50)
        print (result)
        list_of_emails=[]
        for data in result:
            list_of_emails.append(Email(data))

        print (list_of_emails)    
        return list_of_emails
    


    @classmethod
    def delete_one(cls,data):
        query="delete from emails where id=%(id)s"
        result=connectToMySQL(DB).query_db(query,data)
        print (result)
        return result