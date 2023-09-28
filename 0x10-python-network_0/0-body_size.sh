#!/bin/bash
#script that takes in url and send a request to that url
curl -s "$1" | wc -c
