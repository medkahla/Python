from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/users')

@app.route("/users")
def index():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", users=users)
            

@app.route('/user/new')
def add_user():
    return render_template("create.html")

@app.route('/user/create', methods=["post"])
def create():
    User.create(request.form)
    return redirect('/users')






if __name__ == "__main__":
    app.run(debug=True)
