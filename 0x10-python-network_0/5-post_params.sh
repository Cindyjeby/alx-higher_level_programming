#!bin/bash
#script that takes in a url, sends a POST request to the passed url
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"