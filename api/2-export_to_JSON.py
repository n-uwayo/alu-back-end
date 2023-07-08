#!/usr/bin/python3
"""
    python script that exports data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionRequest = requests.Session()

    epId = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(epId)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(epId)

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
    updateUser[epId] = totalTasks

    file_Json = epId + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
