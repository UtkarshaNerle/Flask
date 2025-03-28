from flask import Flask,render_template

app=Flask(__name__)

@app.route('/home')
def home():
    return "welcome to home"

@app.route('/details/<int:id>/<user>')
def details(id,user):
    return render_template("index.html",user_id=id,user_name=user)