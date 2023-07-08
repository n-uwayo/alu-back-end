#!/usr/bin/python3
"""
    python script that exports data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionRequest = requests.Session()

    employeeId = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employeeId)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(employeeId)

    employee = sessionRequest.get(idURL)
    employeeName = sessionRequest.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })
    updateUser[employeeId] = totalTasks

    file_Json = employeeId + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
