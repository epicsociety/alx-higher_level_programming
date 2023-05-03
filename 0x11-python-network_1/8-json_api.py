#!/usr/bin/python3
"""takes in a letter and sends a POST request with the letter as parameter"""


from sys import argv
import requests as request


if __name__ == '__main__':
    URL = 'http://0.0.0.0:5000/search_user'
    if len(argv) >= 2:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}

    req = request.post(URL, data)

    resp = response.headers['content-type']

    if resp == 'application/json':
        result = response.json()
        _id = result.request.get('id')
        name = result.request.get('name')
        if (result != {} and _id and name):
            print("[{}] {}".format(_id, name))
        else:
            print("No result")
    else:
        print('Not a valid JSON')
