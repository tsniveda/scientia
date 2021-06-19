from app import app
from flask import render_template, request, redirect, flash

from flask_mysqldb import MySQL

mysql = MySQL(app)

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/employee-list")
def list_employee(): 
    cur = mysql.connection.cursor() 
    employees = cur.execute("SELECT * FROM employee_details")

    if employees > 0: 
        employeeDetails = cur.fetchall()
    cur.close()

    return render_template("employee_details.html", employeeDetails = employeeDetails)

@app.route("/add-employee-form")
def show_add_employee(): 
    return render_template("add_employee.html")


@app.route("/add-employee", methods=['POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form["name"]
        desg = request.form["desg"]
        addr = request.form["addr"]
        phone = request.form["phone"]

        cur = mysql.connection.cursor() 
        result = cur.execute("INSERT INTO employee_details (emp_name,designation,address,phone) VALUES(%s,%s,%s,%s)",(name, desg, addr, phone))
        mysql.connection.commit()
        cur.close()
        flash("testing flash")
    return redirect("/")