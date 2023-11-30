#!/bin/bash
URL=$1
out=$(curl -s -G $1)
echo $out

