#!/usr/bin/python3
"""  
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import sys
import requests

employee_id = sys.argv[1]

url = "https://jsonplaceholder.typicode.com"

params = {"userId": employee_id}
user = requests.get(url + "/users/{}".format(employee_id)).json()
todos = requests.get(url + "/todos", params).json()

completed_tasks = []  # Initialize completed_tasks list

for task in todos:
    if task.get("completed") is True:
        completed_tasks.append(task.get("title"))

# Print the employee's name and the number of completed tasks
print(
    "Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)
    )
)
# Print the completed tasks one by one with indentation
for complete in completed_tasks:
    print("\t {}".format(complete))
