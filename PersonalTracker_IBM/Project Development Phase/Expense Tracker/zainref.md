dir - website > static, website > template, main.py
files - website > **init**.py, models.py, views.py, auth.py

pip install flask
pip install flask-login
pip install flask-sqlalchemy
pip listx
--------flask --app main.py --debug run

we need to register blueprints from views to init - to import it as package of website

<script
      type="'text/javascript"
      src="{{ url_for('static',filename = 'js/index.js') }}"
></script>

Website colours
-------primary main---------------
offwhite - #fff7e9 rgba(255,247,233,255)
eggyellow - #ffd481 rgba(255,212,129,255)
-------secondary for texts--------
brightred - #d32840 rgba(211,40,64,255)
-------highlights,buttons---------
darkred - #800b2d rgba(128,11,45,255)

{% include 'Navbar.html' %}

-----for inserting icons-------
{% block head %}
{{ super() }}

<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}" 
type="image/x-icon">
<link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}"
type="image/x-icon">

{% endblock %}
