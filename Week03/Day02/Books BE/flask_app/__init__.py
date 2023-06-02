from flask import Flask
app = Flask(__name__)
app.secret_key = "BeltBookThoughts"
DATABASE = "book_club_db"