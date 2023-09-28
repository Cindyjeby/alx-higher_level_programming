#!/bin/bash
#script that takes in a url and displays all HTTP methods
curl -Is "$1" | grep Allow | cut -c 8-
