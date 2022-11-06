from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/')
def landingPage():
    return render_template("landingPage.html")

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/aboutus')
def aboutUs():
    return render_template("aboutUs.html")

@views.route('/contactus')
def contactUs():
    return render_template("contactUs.html")



# stores main views or the url endpoints for the functioning of the frontend aspect
# anything that's not related to authentication and just for navigation