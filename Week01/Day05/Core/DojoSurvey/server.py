from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "safeKey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    session["user"] = request.form["user"]
    session["location"] = request.form["location"]
    session["fav_lang"] = request.form["fav_lang"]
    session["comment"] = request.form["comment"]
    # session["ambition"] = request.form["ambition"]
    # session["gender"] = request.form["radio"]

    return redirect("/result")

@app.route("/result")
def display():
    return render_template("result.html", infos = session)









if __name__ == "__main__":
    app.run(debug=True)