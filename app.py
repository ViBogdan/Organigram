from flask import render_template, request, redirect, url_for
from __init__ import db, app
import models
from print_structure import print_direct_employees


@app.route("/")
@app.route("/index")
def index_page():

    #finds the CEO of the company as being the person to report to the BOARD:
    for instance in db.session.query(models.Employee).filter(models.Employee.reporting_manager == "BOARD"):
        ceo = instance

    organization = [] #our list to be populated

    #populating the organization list with all positions including indentations
    print_direct_employees(ceo, organization)

    return render_template("index.html", organization=organization, ceo=ceo)


@app.route("/add", methods = ["GET", "POST"])
def add_page():
    if request.method == "POST":
        new_name = request.form['new_name']
        new_position = request.form['new_position']
        new_reporting_manager = request.form['new_reporting_manager']

        new_employee = models.Employee(name=new_name, position=new_position, reporting_manager=new_reporting_manager)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('index_page'))

    return render_template("add.html")


@app.route("/update", methods = ["GET", "POST"])
def update_page():

    # current_employees = []
    # for current_employee in db.session.query(models.Employee):
    #     current_employees.append(current_employee) #test

    if request.method == "POST":
        ID = request.form["ID"]
        update_this = models.Employee.query.filter_by(id = ID).first()

        update_name = request.form['update_name']
        update_position = request.form['update_position']
        update_reporting_manager = request.form['update_reporting_manager']

        if update_name:
            update_this.name = update_name
        if update_position:
            update_this.position = update_position
        if update_reporting_manager:
            update_this.reporting_manager = update_reporting_manager

        db.session.commit()
        return redirect(url_for('index_page'))

    return render_template("update.html", current_employees=current_employees)


@app.route("/delete", methods = ["GET", "POST"])
def delete_page():

    current_employees = []
    for current_employee in db.session.query(models.Employee):
        current_employees.append(current_employee)

    if request.method == "POST":
        ID = request.form["ID"]
        delete_this = models.Employee.query.filter_by(id = ID).first()

        if delete_this.position == "Manager" or delete_this.position == "VP":
            for employee in current_employees:
                if employee.reporting_manager == delete_this.name:
                    employee.reporting_manager = delete_this.reporting_manager

        db.session.delete(delete_this)
        db.session.commit()
        return redirect(url_for('index_page'))
    return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug=True)