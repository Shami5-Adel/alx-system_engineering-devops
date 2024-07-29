#!/usr/bin/python3
'''A Python script to export data in the CSV format'''

import re
import requests
import sys

"""The API's URL"""
API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    """Checks if the command line arguments are provided"""
    if len(sys.argv) > 1:
        """Checks if the argument is a valid user ID"""
        if re.fullmatch(r'\d+', sys.argv[1]):
            """Gets the user's information from the API"""
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            user_name = user_res.get('username')

            """Filter todos for the given user"""
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))

            """Writes the data to a CSV file"""
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
