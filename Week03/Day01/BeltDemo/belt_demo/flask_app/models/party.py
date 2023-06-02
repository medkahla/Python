from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Party:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.user_id = data['user_id']
        self.description = data['description']
        self.location = data['location']
        self.all_ages = data['all_ages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self) -> str:
        return f"{self.title}--{self.user_id}"

    # Queries
    @classmethod
    def create_party(cls, data):
        query = """
        INSERT INTO parties (user_id, title, date, description, location, all_ages) 
        VALUES (%(user_id)s,%(title)s,%(date)s,%(description)s,%(location)s,%(all_ages)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = " SELECT * FROM parties; "
        all_parties = []
        results = connectToMySQL(DATABASE).query_db(query)
        for row in results: # type: ignore
            all_parties.append(cls(row))
        print(all_parties)
        return all_parties
    
    # @classmethod
    # def get_by_id(cls, data):
    #     query = """
    #     SELECT * FROM users WHERE id = %(id)s;
    #     """
    #     result = connectToMySQL(DATABASE).query_db(query,data)
    #     return cls(result[0]) # type: ignore
    
    # @classmethod
    # def get_by_email(cls,data):
    #     query = """
    #     SELECT * FROM users WHERE email = %(email)s;
    #     """
    #     result = connectToMySQL(DATABASE).query_db(query,data)
    #     if(result):
    #         return cls(result[0]) # type: ignore
    #     return False

    # * VALIDATIONS 
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['title'])< 2:
            flash("First Name must be at least 3 ")
            is_valid = False
        if len(data['location'])< 2:
            flash("Location is required !!!!!!!")
            is_valid = False
        if len(data['description'])< 9:
            flash("Description is too short")
            is_valid = False
        elif data['date'] == "":
            flash("Date is required !!!!!!!")
            is_valid = False
        return is_valid