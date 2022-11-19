from flask import Blueprint,render_template

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template("Login")

@auth.route('/logout')
def logout():
    return render_template("logout")

@auth.route('/signin')
def signin():
    return render_template("signIn.html")

@auth.route('/signup')
def signup():
   return render_template("signUp.html")