from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash, session
from flask_app.models import user

class Recipe :
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.user_id = data['user_id']
        self.description = data['description']
        self.instructions = data['instructions']
        self.cooked = data['cooked']
        self.timing = data['timing']
        # self.owner = 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    def __repr__(self) -> str:
        return f"{self.title}--{self.user_id}--{self.description}--{self.instructions}--{self.cooked}--{self.timing}"

    @classmethod
    def create_rep(cls, data):
        query = """
        INSERT INTO recipes (title, user_id, description, instructions, cooked, timing) 
        VALUES (%(title)s, %(user_id)s, %(description)s, %(instructions)s, %(cooked)s, %(timing)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        return result
    
    @classmethod
    def get_link(cls):
        query = """ SELECT recipes.id, title, user_id, timing, first_name 
        FROM recipes JOIN users on user_id = users.id;
        """
        return connectToMySQL(DATABASE).query_db(query)
    
    @classmethod
    def get_one(cls, recipe_id):
        query = """
        SELECT recipes.id, title, user_id, description, instructions, cooked, timing, first_name 
        FROM recipes 
        JOIN users on user_id = users.id WHERE recipes.id = %(id)s;
        """
        data = {'id':recipe_id}
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result[0] # type: ignore
    
    @classmethod
    def update(cls, data):
        query = """
            UPDATE recipes 
            SET title=%(title)s,description=%(description)s,instructions=%(instructions)s,cooked=%(cooked)s,timing=%(timing)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # @classmethod
    # def get_owner(cls, recipe_id):
    #     query = "SELECT first_name FROM recipes JOIN users on user_id = users.id WHERE recipes.id = %(id)s;"
    #     data = {'id':recipe_id}
    #     result = connectToMySQL(DATABASE).query_db(query,data)
    #     return cls(result[0]) # type: ignore

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM recipes where id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, {'id':id})

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['title']) == 0 :
            flash("Your recipe must have a title")
            is_valid = False
        if len(data['description']) == 0:
            flash("How do you descripe it")
            is_valid = False
        if len(data['instructions']) == 0:
            flash("How should we do it")
            is_valid = False
        return is_valid
        