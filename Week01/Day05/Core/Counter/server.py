from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "salem"

@app.route("/")
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template("index.html", count=session['counter'])

@app.route("/destroy")
def reset_counter():
    session.clear()
    return redirect("/")

@app.route("/adding")
def add():
    session["counter"] += 1
    return redirect("/")










if __name__ == "__main__":
    app.run(debug=True)