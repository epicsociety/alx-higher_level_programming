#!/usr/bin/python3
"""Takes in url and email and sends a POST request
with the message as parrameter, and prints the body of the response"""

if __name__ == "__main__":
    import requests as request
    import sys
    email = {'email': sys.argv[2]}
    fetch_data = request.post(sys.argv[1], email)
    print(fetch_data.text)
