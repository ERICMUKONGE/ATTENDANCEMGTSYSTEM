from flask import Flask, redirect,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy 
import os

from requests import session

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

print("\n",BASE_DIR)

class user:
    def __init__(self,id,name,password):
        self.id=id
        self.name=name
        self.password=password 

    def __repr__(self):
        return f'<user: {self.name}>'

users = []
users.append(user(id=1, name='mukonge', password='Senjah@24')) 

#print(users)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(BASE_DIR,"site.sqlite3")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_ECHO"]=True
db = SQLAlchemy(app)

class Student(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    first_name=db.Column(db.String(25),nullable=False)
    last_name=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(25),nullable=False)

    def __init__(self,first_name,last_name,email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email

       

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        #session.pop("user_id", None)

        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))
            
    return render_template("login.html")   



if __name__ == "__main__":
    app.run(debug=True)


