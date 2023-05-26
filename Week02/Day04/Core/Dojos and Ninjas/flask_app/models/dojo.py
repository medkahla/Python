from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja

class Dojo:
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    # CRUD Queries
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for row in results: # type: ignore
            dojos.append(cls(row))
        return dojos
    # Create
    @classmethod
    def add_dojo(cls, data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM dojos WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0]) # type: ignore