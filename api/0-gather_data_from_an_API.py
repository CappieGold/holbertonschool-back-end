#!/usr/bin/python3

import requests
import sys

def fetch_todo_progress(employee_id):
    # Endpoint URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to retrieve data for employee ID {employee_id}")
        return

    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch TODOs for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task['completed'])
    
    # Print progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_todo_progress(employee_id)
