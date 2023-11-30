#!/bin/bash
#bash script that print num of bytes received
curl -w '%{size_download}\n' -s "$1" -o /dev/null
