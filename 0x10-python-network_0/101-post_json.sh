#!/usr/bash
# script that sends a JSON POST request to a URL
# URL passed as the first argument,
# and displays the body of the response
curl -s -X POST -H "content_type:application/json" -d @"$2" "$1"
