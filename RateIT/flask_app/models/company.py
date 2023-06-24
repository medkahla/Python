from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, UPLOAD_FOLDER
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


#--------CLASS COMPANY
class Company:
#--------CONSTRUCTOR
    def __init__(self,data):
        self.id = data['id']
        self.sector_id = data['sector_id']
        self.adress_id = data['adress_id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.logo = UPLOAD_FOLDER+str(data['logo'])
        self.site = data['site']
        self.mf=data['mf']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sector = ""
        self.adress = ""

#--------CRUD
#--------READ ALL COMPANIES
    @classmethod
    def get_all(cls):
        query = """
        SELECT companies.*, sectors.title AS sector FROM companies
        JOIN sectors ON sector_id = sectors.id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        companies  = []
        if results:
            for row in results:
                comp = cls(row)
                comp.sector = row["sector"]
                companies.append(comp)
        return companies
    
#----------CREATE COMPANY
    @classmethod
    def add_company(cls, data):
        query = """
        INSERT INTO companies (sector_id, adress_id, name, mf, site, email, password) 
        VALUES (%(sector_id)s,%(adress_id)s, %(name)s, %(mf)s, %(site)s, %(email)s, %(password)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #----------UPDATE COMPANY
    @classmethod
    def edit_company(cls, data):
        query = """
        UPDATE companies SET sector_id = %(sector_id)s, email = %(email)s, name= %(name)s,logo=%(logo)s,site=%(site)s,mf=%(mf)s, password=%(password)s 
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #----------DELETE COMPANY
    @classmethod
    def delete_company(cls, data):
        query = """
        delete from companies where id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #---------GET BY ID
    @classmethod
    def get_by_id(cls,data):
        query= """
        SELECT * FROM companies WHERE id= %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    
    #---------GET BY Name
    @classmethod
    def get_by_name(cls,data):
        query= """
        SELECT id FROM companies WHERE title= %(title)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    
    #---------GET BY Email
    @classmethod
    def get_by_email(cls,data):
        query = """
        SELECT * FROM companies WHERE email = %(email)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        if(result):
            return cls(result[0])
        return False
    
    @classmethod
    def get_all_with_sector(cls,data):
        query = """
        SELECT companies.*, sectors.title AS sector 
        FROM companies
        JOIN sectors ON sector_id = sectors.id
        WHERE sector_id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        companies  = []
        if results:
            for row in results:
                comp = cls(row)
                comp.sector = row["sector"]
                companies.append(comp)
        return companies

    @classmethod
    def count(cls):
        query="SELECT COUNT(*) AS companies_number FROM companies;"
        result = connectToMySQL(DATABASE).query_db(query)
        return result[0]['companies_number']
    
    @classmethod
    def search(cls, data):
        query=""" SELECT companies.*, sectors.title as sector 
        FROM companies JOIN sectors
        ON sector_id = sectors.id
        WHERE name like %(word)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        result = []
        if results:
            for row in results:
                comp = cls(row)
                comp.sector = row["sector"]
                result.append(comp)
        return result

    @classmethod
    def get_for_index(cls):
        query=""" 
        SELECT companies.*, sectors.title as sector, 
        CONCAT(adresses.number," ",adresses.street," ",adresses.zipcode) AS adress FROM companies 
        JOIN sectors ON sector_id = sectors.id
        JOIN adresses ON adress_id = adresses.id
        ORDER BY companies.created_at DESC LIMIT 6;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        result = []
        if results:
            for row in results:
                comp = cls(row)
                comp.sector = row["sector"]
                comp.adress = row["adress"]
                result.append(comp)
        return result

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name'])< 2:
            flash("First Name must be at least 3 caracters", "campReg")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "campReg")
            is_valid = False
        elif Company.get_by_email({'email':data['email']}):
            flash("Email address already used, try login", "campReg")
            is_valid = False
        if len(data['password'])< 6:
            flash("Password too short", "campReg")
            is_valid = False
        elif data['password'] != data['confirm_password']:
            flash("Password does not match ", "campReg")
            is_valid = False
        return is_valid
    