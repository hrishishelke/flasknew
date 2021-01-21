import self as self
from flask import Flask, render_template, request, redirect, session
import mysql.connector

app=Flask(__name__)

conn =mysql.connector.connect(host="localhost",user="root",password="",database="hrishikesh")
cursor =conn.cursor()



@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login_validation',methods=['post'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM 'name' WHERE 'email' LIKE '{}' AND 'password' LIKE '{}'"""
                .format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
       return render_template('home.html')
    else:
       return render_template('login.html')


@app.route('/register',methods=['post'])
def register():

     return "Registration Succesfully !"


@app.route('/logout')
def logout():
     session.pop('user_id')
     return redirect('/')

if __name__=="__main__":
     app.run(debug=True)