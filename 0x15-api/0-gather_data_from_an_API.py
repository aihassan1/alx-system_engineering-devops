#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""
import requests
import sys

# Get employee ID from command line argument
employee_id = sys.argv[1]

# Base URL for the JSONPlaceholder API
url = "https://jsonplaceholder.typicode.com"

# Parameters to filter TODO list by employee ID
params = {"userId": employee_id}

# Retrieve user information for the given employee ID
user = requests.get(url + "/users/{}".format(employee_id)).json()

# Retrieve TODO list for the given employee ID
todos = requests.get(url + "/todos", params).json()

# Initialize a list to store titles of completed tasks
completed_tasks = []

# Iterate over each TODO item
for task in todos:
    # Check if the task is completed
    if task.get("completed") is True:
        # Append the title of the completed task to the list
        completed_tasks.append(task.get("title"))

# Print the employee's name and the number of completed tasks
print(
    "Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)
    )
)

# Print the titles of completed tasks with indentation
for complete in completed_tasks:
    print("\t {}".format(complete))
