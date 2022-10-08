from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.debug = True
 
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
 
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
 
    def __repr__(self):
        return f"email : {self.email}, password: {self.password}"

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    profiles = Profile.query.all()
    return render_template('index.html', profiles=profiles)
 

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/signup")
def signup():   
    return render_template('signup.html')
 

@app.route('/add', methods=["POST"])
def profile():
    email = request.form.get("email")
    password = request.form.get("password")
 
    if email != '' and password != '':
        p = Profile(email=email, password=password)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')
 
@app.route('/delete/<int:id>')
def erase(id):
     
    data = Profile.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')
 
if __name__ == '__main__':
    app.run()

