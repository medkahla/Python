from flask import Flask, render_template
app = Flask(__name__)    

@app.route("/")          
def hello_world():
    return "Hello World! \n <h1>Ready to play?!</h1>"

@app.route("/play")
def play():
    return render_template("index.html")

@app.route("/play/<int:num>")
def multipleB(num):
    return render_template("index.html", x=num)

@app.route("/play/<int:num>/<color>")
def coloret(num, color):
    col =str(color)
    return render_template("index.html", x=num, c=col)


if __name__=="__main__":   
    app.run(debug=True)