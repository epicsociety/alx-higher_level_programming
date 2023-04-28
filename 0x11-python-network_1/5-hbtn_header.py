#!/usr/bin/python3
""" fetches the url as follows"""


if __name__ == '__main__':
    import requests as request
    import sys
    url = sys.argv[1]
    fetch_url = request.get(url)
    resp = fetch_url.headers.get('X-Request-Id')
    print(resp)
