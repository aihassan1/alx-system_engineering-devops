#!/usr/bin/python3

"""
returns information about his/her TODO list progress.
export data in the CSV format

USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE
"""
import csv
import requests
import sys

if __name__ == "__main__":
    # Get employee ID from command line argument
    employee_id = sys.argv[1]

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com"

    # Retrieve user information for the given employee ID
    user = requests.get(url + "/users/{}".format(employee_id)).json()
    user_id = user.get("id")
    user_name = user.get("name")

    # Parameters to filter TODO list by employee ID
    params = {"userId": employee_id}

    # Retrieve TODO list for the given employee ID
    todos = requests.get(url + "/todos", params).json()

    # Initialize a list to store task information
    values_list = []

    # Iterate over each TODO item
    for task in todos:
        TASK_COMPLETED_STATUS = task.get("completed")
        TASK_TITLE = task.get("title")
        values_list.append([employee_id, user_name, TASK_COMPLETED_STATUS, TASK_TITLE])

    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for value in values_list:
            writer.writerow(value)
