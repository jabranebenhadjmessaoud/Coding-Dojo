from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    
    @classmethod
    def get_all(cls):
        query="select * from users ;"
        result=connectToMySQL("users_schema").query_db(query)
        print("@"*50)
        print (result)
        list_of_users=[]
        # user1=User(result[0])
        # print("*"*20)
        # print(user1.first_name)
        # print("*"*20)
        for data in result:
            list_of_users.append(User(data))

        print (list_of_users)    
        return list_of_users
    
    @classmethod
    def create(cls,data):
        query="""insert into users (first_name, last_name, email)
        values (%(first_name)s,%(last_name)s,%(email)s);"""
        result=connectToMySQL("users_schema").query_db(query,data)
        return result 
    

    @classmethod
    def delete_one(cls,data):
        query="delete from users where id=%(id)s"
        result=connectToMySQL("users_schema").query_db(query,data)
        print (result)
        return result



    @classmethod
    def show_one(cls,data):
        query="select * from users where id=%(id)s;"
        result=connectToMySQL("users_schema").query_db(query)
        usertoshow=User(result)
        print (usertoshow)
        return usertoshow
        