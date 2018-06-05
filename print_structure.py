from __init__ import db
from models import Employee


#core logic
def print_direct_employees(instance, the_list, level=0):
    the_list.append("{}{} as {}({})".format(" " * level * 4, instance.name, instance.position, instance.id))
    for direct_employee in db.session.query(Employee).filter(Employee.reporting_manager == instance.name):
        print_direct_employees(direct_employee, the_list, level+1)
    return the_list


# un-comment to activate testing of core logic:

# final_list = []
# for instance in db.session.query(Employee).filter(Employee.reporting_manager == "BOARD"):
#     print_direct_employees(instance, final_list)
#
# for element in final_list:
#     print(element)
