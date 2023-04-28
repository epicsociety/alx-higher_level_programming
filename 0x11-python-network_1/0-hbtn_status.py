#!/usr/bin/python3
"""modules fetches the given url and print some stuff"""
if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        html = resp.read()

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
