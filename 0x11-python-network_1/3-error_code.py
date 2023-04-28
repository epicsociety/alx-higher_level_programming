#!/usr/bin/python3
"""takes in a URL, sends a request to it and displays
 the body of the response"""


if __name__ == "__main__":
    import urllib.request as request
    import urllib.error as error
    import sys
    url_req = request.Request(sys.argv[1])
    try:
        with request.urlopen(url_req) as resp:
            html = resp.read().decode('utf-8')
            print(html)
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
