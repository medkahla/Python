from flask import Flask
from datetime import date

app = Flask(__name__)
app.secret_key = "PythonBeltAppointments"
DATABASE = "appointments_db"

TODAY = date.today()

print(TODAY,"--*--"*20)