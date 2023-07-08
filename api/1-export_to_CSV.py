#!/usr/bin/python3
"""
    python script that exports data in the CSV format
"""

import csv
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

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    fileCSV = employeeId + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_req:
            write.writerow([employeeId, usr, i.get('completed'), i.get('title')])
