#!/usr/bin/python3
"""Script using API and module requests"""


import json
import requests
import sys


def export_tasks_to_json(employee_id):
    """json format"""

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/\
todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)

    user_data = user_response.json()
    username = user_data['username']

    # Fetch tasks for the user
    todos_response = requests.get(todos_url)

    todos_data = todos_response.json()

    # Prepare data for JSON format
    tasks_info = []
    for task in todos_data:
        tasks_info.append({"task": task['title'], "completed":
                           task['completed'], "username": username})

    # Create JSON structure
    json_output = {str(employee_id): tasks_info}

    # Write data to JSON file
    with open(f"{employee_id}.json", 'w') as json_file:
        json.dump(json_output, json_file)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_tasks_to_json(employee_id)
