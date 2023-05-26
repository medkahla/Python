from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import dojo

class Ninja:
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.age = data_dict['age']
        self.dojo_id = data_dict['dojo_id']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    # CRUD Queries
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for row in results: # type: ignore
            ninjas.append(cls(row))
        return ninjas
    
    # Create
    @classmethod
    def add_ninja(cls, data):
        query = """
        INSERT INTO ninjas (first_name,last_name, age, dojo_id)
        VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_list(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        ninjas = []
        if(results):
            for row in results: # type: ignore
                ninjas.append(cls(row))
            return ninjas
        else:
            return []   