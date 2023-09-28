#!/bin/bash
#script taht sends request to url passed as an argument
curl -s -o /dev/null -w "%{http_code}" "$1"
