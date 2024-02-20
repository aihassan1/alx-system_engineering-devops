#!/usr/bin/python3

"""
Python script that retrieves TODO list data from the
JSONPlaceholder API and exports it in JSON format.
"""

import json
import requests

if __name__ == "__main__":
    # Retrieve TODO list data from the API
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todos_data = todo_response.json()

    # Retrieve users data from the API
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users_data = users_response.json()

    # Create a dictionary to store TODO list data grouped by user ID
    todos_by_user = {}

    # Iterate over each user
    for user in users_data:
        user_id = user["id"]
        username = user["username"]

        # Initialize a list to store TODO items for this user
        user_todos = []

        # Iterate over each TODO item
        for todo in todos_data:
            # Check if the TODO item belongs to the current user
            if todo["userId"] == user_id:
                # Create a dictionary to represent the TODO item
                todo_item = {
                    "username": username,
                    "task": todo["title"],
                    "completed": todo["completed"],
                }
                # Append the TODO item to the list of user's TODOs
                user_todos.append(todo_item)

        # Add the list of user's TODOs to the dictionary
        todos_by_user[user_id] = user_todos

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todos_by_user, json_file)
