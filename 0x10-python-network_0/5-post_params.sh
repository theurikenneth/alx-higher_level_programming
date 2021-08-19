#!/bin/bash
# scripts that takes in a URL, sends a POST request to the
# passed URL, and displays the response body
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
