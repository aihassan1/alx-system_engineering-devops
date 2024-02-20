#!/usr/bin/python3

"""returns information about his/her TODO list progress."""
import json
import requests


if __name__ == "__main__":
    # Get user_id from command line argument

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com"

    # Parameters to filter TODO list by user_id

    # Retrieve user information for the given user_id ID
    users = requests.get(url + "/users/").json()

    for user in users:
        user_id = user["id"]
        user_name = user["username"]
        params = {"userId": user_id}
        # Retrieve TODO list for the given user_id
        todos = requests.get(url + "/todos", params).json()

        todo_list = []  # Initialize a list to store todo dictionaries

        for task in todos:
            TASK_COMPLETED_STATUS = task.get("completed")
            TASK_TITLE = task.get("title")
            USERNAME = user_name

            todo_dict = {
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME,
            }

            todo_list.append(todo_dict)

            all_tasks = {user_id: todo_list}

        with open("todo_all_employees.json", "a") as file:
            json.dump(all_tasks, file)
