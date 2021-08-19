#!/bin/bash
# bash script tat takes in an URL, sends a request
# to that URL and displays the size of the body of the response

curl -w '%{size_download}\n' -so /dev/null $1
