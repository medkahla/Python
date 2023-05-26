from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Book:
    def __init__(self, data_dict):
        self.id = data_dict["id"]
        self.title = data_dict["title"]
        self.pages = data_dict["pages"]
        self.created_at = data_dict["created_at"]
        self.updated_at = data_dict["updated_at"] 
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def create_book(cls, data):
        query = """
        INSERT INTO books (title, pages)
        VALUES (%(title)s,%(pages)s)
        """
        return connectToMySQL(DATABASE).query_db(query, data)

