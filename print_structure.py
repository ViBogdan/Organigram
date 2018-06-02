from __init__ import db
from models import Employee


def print_direct_employees(instance, level=0):
    print("{}{}".format(" " * level * 4, instance.name))
    for direct_employee in db.session.query(Employee).filter(Employee.reporting_manager == instance.name):
        print_direct_employees(direct_employee, level+1)


for instance in db.session.query(Employee).filter(Employee.reporting_manager == "BOARD"):
    print_direct_employees(instance)
