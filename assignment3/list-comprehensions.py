# Task 3

import csv

with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    employees = list(reader)

  
names = [row[1] + " " + row[2] for row in employees[1:]]
print(names)  


names_with_e = [name for name in names if "e" in name]
print(names_with_e)