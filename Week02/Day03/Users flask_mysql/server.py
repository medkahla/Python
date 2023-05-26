from flask import Flask, render_template, redirect, request
# import the class from user.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all Userss
    user = User.get_all()
    print(user)
    return render_template("read_all.html")
            
if __name__ == "__main__":
    app.run(debug=True)

