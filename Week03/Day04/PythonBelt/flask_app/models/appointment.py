from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import TODAY
from flask import flash
from datetime import datetime

class Appointment:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.poster = ""
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_this_user(cls, data):
        query = """
        SELECT appointments.id, appointments.user_id, appointments.task, appointments.date, appointments.status, users.first_name AS poster 
        FROM appointments JOIN users ON user_id = users.id
        WHERE user_id = %(id)s; 
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def create_appointment(cls, data):
        query = """
        INSERT INTO appointments (user_id, task, date, status) 
        VALUES (%(user_id)s,%(task)s,%(date)s,%(status)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data) 

    @classmethod
    def get_by_id(cls, id):
        query = """
        SELECT * FROM appointments WHERE id = %(id)s;
        """
        data = {'id':id}
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0]) # type: ignore 
    
    @classmethod
    def get_one_with_user(cls, id):
        query = """
        SELECT appointments.id, user_id, task, date, status, first_name AS poster
        FROM appointments JOIN users on user_id = users.id 
        WHERE appointments.id = %(id)s;
        """
        data = { 'id':id }
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result[0] # type: ignore
    
    @classmethod
    def update(cls, data):
        query = """
        UPDATE appointments SET task=%(task)s, date=%(date)s, status=%(status)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def destroy_appointment(cls, id):
        query = """
        DELETE FROM appointments WHERE id = %(id)s;
        """
        data = {
            'id':id
        }
        return connectToMySQL(DATABASE).query_db(query,data)

    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['task'])< 2:
            flash("Title is required!!")
            is_valid = False
        if len(data['date'])< 2:
            flash("When?!")
            is_valid = False
        elif data['date'] < str(TODAY):
            flash("You're adding an appointments in the past!")
            is_valid = False
        if len(data['status']) <2:
            flash("The status is required")
            is_valid = False
        return is_valid

