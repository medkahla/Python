from flask import Flask
app = Flask(__name__)
app.secret_key = "ba35iiir"
DATABASE = "recipes_exam_db"