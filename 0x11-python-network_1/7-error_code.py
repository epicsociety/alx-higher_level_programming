#!/usr/bin/python3
"""takes in a URL, sends a request to it and displays
 the body of the response"""


if __name__ == "__main__":
    import requests as request
    import sys
    fetch_res = request.get(sys.argv[1])
    if fetch_res.status_code >= 400:
        print("Error code: {}".format(fetch_res.status_code))
    else:
        print(fetch_res.text)
