#!/usr/bin/python3
"""Evaluates a candidate's github commits"""


import sys
from requests import get


if __name__ == '__main__':
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    i = 0

    url = "https://api.github.com/repos/{}/{}/commits".
    format(owner_name, repository_name)

    resp = get(url)
    json = resp.json()

    for element in json:
        if i > 9:
            break
        sha = element.get('sha')
        author = element.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        i += 1
