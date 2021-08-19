#!/bin/bash
# bash script that sends a DELETE request to the URL
# passed as the first argument and displays response body
curl -s -X "DELETE" "$1"
