from flask import Flask,render_template

app=Flask(__name__)

@app.route('/home')
def home():
    return "welcome to home"

@app.route('/details')
def details():
    return render_template("index.html")