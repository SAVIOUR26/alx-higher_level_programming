#!/bin/bash
# sending a JSON POST request to a URL passed as the first argument, and displaying the body of the response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
