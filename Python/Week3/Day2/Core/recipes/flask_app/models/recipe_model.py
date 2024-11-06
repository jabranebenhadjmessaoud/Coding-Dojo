from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash



class Recipe :
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.date=data['date']
        self.under_time=data['under_time']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.posted_by=""
    
    
    @classmethod 
    def add_recipe(cls,data):
        query="""
                insert into recipes (name, description, instructions, date, under_time, user_id)
                values (%(name)s, %(description)s, %(instructions)s,%(date)s, %(under_time)s, %(user_id)s);
                """
        return connectToMySQL(DB).query_db(query,data)
    




    @classmethod
    def get_all(cls):
        query=""" select * from recipes 
                    join users on recipes.user_id=users.id ;"""
        results=connectToMySQL(DB).query_db(query)
        all_recipes=[]
        for row in results :
            recipe=cls(row)
            recipe.posted_by=f'{row["first_name"]} {row["last_name"]}'
            all_recipes.append(recipe)
        return all_recipes

    @classmethod
    def get_by_id(cls,data):
        query=""" select * from recipes 
                    join users on recipes.user_id=users.id 
                    where recipes.id=%(id)s;"""
        result=connectToMySQL(DB).query_db(query,data)
        
        recipe=cls(result[0])
        recipe.posted_by=f'{result[0]["first_name"]}'
        
        return recipe    

    @classmethod
    def delete(cls,data):
        query="delete from recipes where id=%(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def update(cls,data):
        query=""" update recipes set
                name=%(name)s,
                description=%(description)s,
                instructions=%(instructions)s,
                date=%(date)s,
                under_time=%(under_time)s
                where id=%(id)s;  
                """
        return connectToMySQL(DB).query_db(query,data)




    @staticmethod
    def validate_recipe(data):
        is_valid=True
        if len (data['name'])<3 :
            flash ("Name must be longer than 2 characters","recipe_flashes")
            is_valid =False
        if len (data['description'])<3 :
            flash ("description must be longer than 2 characters","recipe_flashes")
            is_valid =False
        if len (data['instructions'])<3 :
            flash ("instructions must be longer than 2 characters","recipe_flashes")
            is_valid =False
        if data['date']==None:
            flash ("date must be empty","recipe_flashes")
            is_valid =False
        return is_valid
    