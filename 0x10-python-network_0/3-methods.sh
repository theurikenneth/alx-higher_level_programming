#!/bin/bash
# script that takes in a URL and displays all HTTP
curl -s -I "$1" | grep Allow | cut -d' ' -f2-
