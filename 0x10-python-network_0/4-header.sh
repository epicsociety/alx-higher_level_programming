#!/bin/bash
# takes in a URL passed, sends a GET request, displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
