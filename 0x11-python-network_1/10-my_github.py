#!/usr/bin/python3
"""using github API to authenticate a user"""


import sys
import requests as request


if __name__ == "__main__":
    url = "https://api.github.com/user"
    if len(sys.argv) > 2:
        username = sys.argv[1]
        password = sys.argv[2]
        headers_req = {
                'Accept': 'application/vnd.github.v3+json',
                'Username': username,
                'Authorization': 'token {}'.format(password),
                }
        resp = request.get(url, headers=headers_req)
        if resp.status_code == 200:
            user = resp.json()
            if user['login'] == username:
                print(user['id'])
            else:
                print('None')
        else:
            print('None')
