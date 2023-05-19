from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/<int:numR>")
# def row(numR):
#     return render_template("index.html", nr=numR)

# @app.route("/<int:numR>/<int:numC>")
# def column(numR, numC):
#     return render_template("index.html", nr=numR, nc=numC)

# @app.route("/<int:numR>/<int:numC>/<firstC>")
# def color1(numR, numC, firstC):
#     return render_template("index.html", nr=numR, nc=numC, fc=firstC)

# @app.route("/<int:numR>/<int:numC>/<firstC>/<secondC>")
# def color2(numR, numC, firstC, secondC):
#     return render_template("index.html", nr=numR, nc=numC, fc=firstC, sc=secondC)


if __name__ == "__main__":
    app.run(debug=True, port=5001)