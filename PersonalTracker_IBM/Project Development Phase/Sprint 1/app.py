from flask import Flask, request, redirect
from flask import Blueprint,render_template
app = Flask(__name__)

app.debug = True

@app.route('/')
def landingPage():
    return render_template("landingPage.html")

@app.route('/navbar')
def navbar():
    return render_template("Navbar.html")


@app.route('/contactus')
def contactus():
    return render_template("contactUs.html")

@app.route('/signup')
def signup():
    return render_template("signUp.html")

@app.route('/signin')
def signin():
    return render_template("signIn.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutUs.html")

@app.route('/skeleton')
def skeleton():
    return render_template("skeleton.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/addingExpenses')
def addingExpenses():
    return render_template("addingExpenses.html")
    
    
if __name__ == '__main__':
    app.run()




