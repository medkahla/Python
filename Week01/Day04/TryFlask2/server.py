from flask import Flask
app = Flask(__name__)    

# 1
@app.route('/')          
def hello_world():
    return 'Hello World!'  

# 2
@app.route('/dojo')
def dojo():
    return "Dojo"

# 3
@app.route("/say/<name>")
def hi(name):
    return f"Hi {name}!"

# 4
@app.route("/repeat/<num>/<word>")
def repeat(num, word):
    return f"<h1>{word}</h1>" * int(num)





if __name__=="__main__":   
    app.run(debug=True)
