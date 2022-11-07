from flask import Flask, render_template
from markupsafe import escape 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/user/<username>')
def show_user_profile(username):
    #show user profile for that user
    #return "Hello, "+ username 
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show post with the given id, the id is an integer
    return f'Post {escape(post_id)}'
    