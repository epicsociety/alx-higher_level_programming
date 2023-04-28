#!/bin/bash
# sends a request to a URL passed, displays only the status code of the response.
curl -sLw "%{response_code}" "$1" -o /dev/null
