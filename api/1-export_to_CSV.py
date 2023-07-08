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

    epId = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(epId)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(epId)

    employee = sessionRequest.get(idURL)
    employeeName = sessionRequest.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    fileCSV = epId + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_req:
            write.writerow([epId, usr, i.get('completed'), i.get('title')])
