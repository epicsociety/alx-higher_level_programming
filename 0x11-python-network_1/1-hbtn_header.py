#!/usr/bin/python3
"""sends a request to the URL passed and dispays the value of the 
X-request-Id variable found in the header of the response
"""
if __name__ == "__main__":
    import urllib.request as request
    import sys
    url = request.Request(sys.argv[1])
    with request.urlopen(url) as req:
        print(req.headers.get("X-Request-Id"))
