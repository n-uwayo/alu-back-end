#!/usr/bin/python3
import sys
import requests

def fetch_todo_list_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)
        employee_response.raise_for_status()
        todos_response.raise_for_status()
        
        employee_data = employee_response.json()
        todos_data = todos_response.json()

        employee_name = employee_data['name']
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task['completed']]

        print(f'Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):')

        for task in completed_tasks:
            print('\t', task['title'])

    except requests.exceptions.RequestException as e:
        print('Error occurred:', str(e))
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 gather_data_from_an_API.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
