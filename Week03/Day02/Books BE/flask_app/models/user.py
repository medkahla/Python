from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Queries
    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (name, email, password) 
        VALUES (%(name)s,%(email)s,%(password)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    def __repr__(self) -> str:
        return f"{self.name}"
    
    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM users WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0]) # type: ignore
    
    @classmethod
    def get_by_email(cls,data):
        query = """
        SELECT * FROM users WHERE email = %(email)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        if(result):
            return cls(result[0]) # type: ignore
        return False

    # * VALIDATIONS 
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name'])< 2:
            flash("Name is required !!!!!!!", "Register")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "Register")
            is_valid = False
        elif User.get_by_email({'email':data['email']}):
            flash("Email address already used , hope by you!","Register")
            is_valid = False
        if len(data['password'])< 6:
            flash("Password too short","Register")
            is_valid = False
        elif data['password'] != data['confirm_password']:
            flash("Password must match ","Register")
            is_valid = False
        return is_valid