#!/usr/bin/python3
"""
    python script that returns TODO list progress for a given employee ID
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
    name = employeeName.json()['name']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
