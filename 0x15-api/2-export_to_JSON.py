#!/usr/bin/python3
"""A Python script to export data in the JSON format"""

import json
import re
import requests
import sys

"""The base URL of the JSONPlaceholder API"""
API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    """
    Check if command line arguments were provided and proceed accordingly.
    """
    if len(sys.argv) > 1:
        """
        Check if the provided argument is a valid user ID (numerical).
        """
        if re.fullmatch(r'\d+', sys.argv[1]):
            """
            Extracts the user ID and convert it to an integer.
            """
            id = int(sys.argv[1])

            """
            Makes an API call to retrieve the user information based
            on the provided user ID.
            """
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()

            """
            Makes another API call to retrieve todos (tasks)
            associated with the user.
            """
            todos_res = requests.get('{}/todos'.format(API_URL)).json()

            """
            Extracts the username of the user from the response.
            """
            user_name = user_res.get('username')

            """Filters todos for the given user"""
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))

            """Writes the data to a JSON file"""
            with open('{}.json'.format(id), 'w') as file:
                """
                Maps todos to the desired JSON format for better organization.
                """
                user_name = user_res.get('username')

            """Filters todos for the given user"""
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))

            """Writes the data to a JSON file"""
            with open('{}.json'.format(id), 'w') as file:
                """
                Maps todos to the desired JSON format for better organization.
                """
                user_data = list(map(
                    lambda x: {
                        'task': x.get('title'),
                        'completed': x.get('completed'),
                        'username': user_name
                    },
                    todos
                ))
                users_data = {
                    '{}'.format(id): user_data
                }

                """
                Writes the structured JSON data to the file.
                """
                json.dump(users_data, file, indent=4)
