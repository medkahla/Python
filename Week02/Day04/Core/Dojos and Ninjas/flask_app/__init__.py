from flask import Flask
app = Flask(__name__)
app.secret_key = "salem"
DATABASE = "dojos_ninjas_schema"