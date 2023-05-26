from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.username = data["username"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"] 
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for row in results: # type: ignore
            users.append(cls(row))
        return users
    
    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (username, age)
        VALUES (%(username)s,%(age)s)
        """
        return connectToMySQL(DATABASE).query_db(query, data)

