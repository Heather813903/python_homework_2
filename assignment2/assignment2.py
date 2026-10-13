import csv
import traceback
from datetime import datetime

# Task 2


def read_employees():
    employee_dict = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as employee_file:
            reader = csv.reader(employee_file)
            first_row = True
            for row in reader:
                if first_row:
                    employee_dict["fields"] = row
                    first_row = False
                else:
                    rows.append(row)

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

    employee_dict["rows"] = rows

    return employee_dict

employees = read_employees()
print(employees)

# Task 3

def column_index(column_name):
    return employees["fields"].index(column_name)
employee_id_column = column_index("employee_id")

# Task 4


def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

# Task 5


def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches

# Task 6

def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"],
        )
    )
    return matches

# Task 7

# Task 7


def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]


sort_by_last_name()
print(employees)

# Task 8

def employee_dict(row):
    employee = {}

    for index in range(len(employees["fields"])):
        if employees["fields"][index] != "employee_id":
            employee[employees["fields"][index]] = row[index]

    return employee


print(employee_dict(employees["rows"][0]))


# Task 9

def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)

    return all_employees
print (all_employees_dict())

# Task 10

import os

def get_this_value():
    return os.getenv("THISVALUE")


# Task 11

import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("beach_girl")
print(custom_module.secret)


# Task 12

def read_minutes():
    def read_file(filename):
        minutes = {"fields": [], "rows": []}

        with open(filename, "r") as file:
            reader = csv.reader(file)
            first_row= True

            for row in reader:
                if first_row:
                    minutes["fields"] = row
                    first_row = False
                else:
                    minutes["rows"].append(tuple(row))

        return minutes

    minutes1 = read_file("../csv/minutes1.csv")
    minutes2 = read_file("../csv/minutes2.csv")

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)


# Task 13

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined = set1.union(set2)

    return combined

minutes_set = create_minutes_set()

# Task 14

def  create_minutes_list():
   minutes = list(minutes_set)
   minutes = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes))

   return minutes

minutes_list = create_minutes_list()
print (minutes_list)


# Task 15

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list

write_sorted_list()