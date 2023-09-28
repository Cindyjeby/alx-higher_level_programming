#!/bin/bash
#script that sends a JSON POST request to url passed as first argument
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
