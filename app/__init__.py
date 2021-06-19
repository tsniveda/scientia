from flask import Flask

from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "swamiyogi"

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = 'swamiyogi@20'
app.config['MYSQL_DB'] = 'employeedb'

from app import employee_views