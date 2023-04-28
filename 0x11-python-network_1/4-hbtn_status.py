#!/usr/bin/python3
""" fetches the url as follows"""


if __name__ == '__main__':
    import requests as request
    fetch_data = request.get("https://alx-intranet.hbtn.io/status")
    fetch_text = fetch_data.text
    print("Body response:")
    print("\t- type: {}".format(type(fetch_text)))
    print("\t- content: {}".format(fetch_text))
