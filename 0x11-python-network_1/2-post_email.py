#!/usr/bin/python3
"""Takes in url and email and sends a POST request
with the message as parrameter, and prints the body of the response"""

if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    import sys
    email = {'email': sys.argv[2]}
    data = parse.urlencode(email).encode('utf-8')
    req_url = sys.argv[1]
    with request.urlopen(req_url, data) as resp:
        print(resp.read().decode('utf-8'))
