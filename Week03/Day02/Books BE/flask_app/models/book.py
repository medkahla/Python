from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.author = data['author']
        self.thought = data['thought']
        self.poster = ""
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
        SELECT books.id, books.user_id, books.title, books.author, users.name AS poster 
        FROM books JOIN users ON user_id = users.id; 
        """
        return connectToMySQL(DATABASE).query_db(query)

    @classmethod
    def create_book(cls, data):
        query = """
        INSERT INTO books (user_id, title, author, thought) 
        VALUES (%(user_id)s,%(title)s,%(author)s,%(thought)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data) 

    @classmethod
    def get_by_id(cls, id):
        query = """
        SELECT * FROM books WHERE id = %(id)s;
        """
        data = {'id':id}
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0]) # type: ignore 
    
    @classmethod
    def get_one_with_user(cls, book_id):
        query = """
        SELECT books.id, user_id, title, author, thought, name AS poster
        FROM books JOIN users on user_id = users.id 
        WHERE books.id = %(id)s;
        """
        data = { 'id':book_id }
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result[0] # type: ignore
    
    @classmethod
    def update(cls, data):
        query = """
        UPDATE books SET title=%(title)s, author=%(author)s, thought=%(thought)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def destroy_book(cls, book_id):
        query = """
        DELETE FROM books WHERE id = %(id)s;
        """
        data = {
            'id':book_id
        }
        return connectToMySQL(DATABASE).query_db(query,data)

    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['title'])< 2:
            flash("Title is required!!")
            is_valid = False
        if len(data['author'])< 2:
            flash("Who wrote it?!")
            is_valid = False
        elif len(data['thought']) <5:
            flash("What do you think about it")
            is_valid = False
        return is_valid

