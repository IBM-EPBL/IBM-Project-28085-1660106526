from flask import Blueprint,render_template


views = Blueprint('views',__name__)

@views.route('/')
def landingPage():
    return render_template("landingPage.html")

@views.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@views.route('/aboutus')
def aboutUs():
    return render_template("aboutUs.html")

@views.route('/contactus')
def contactUs():
    return render_template("contactUs.html")

@views.route('/transactions')
def transactions():
    return render_template("transactions.html")

@views.route('/addingExpenses')
def addingExpenses():
    return render_template("addingExpenses.html")

@views.route('/categories')
def categories():
    return render_template("categories.html")

@views.route('/reports')
def reports():
    return render_template("reports.html")

@views.route('/tips')
def tips():
    return render_template("tips.html")

@views.route('/help&support')
def helpAndSupport():
    return render_template("help&support.html")

@views.route('/settings')
def settings():
    return render_template("settings.html")
    
@views.route('/notifications')
def settnotificationsings():
    return render_template("notifications.html")

@views.route('/skeleton')
def skeleton():
    return render_template("skeleton.html")


# stores main views or the url endpoints for the functioning of the frontend aspect
# anything that's not related to authentication and just for navigation