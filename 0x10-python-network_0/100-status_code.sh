#!/bin/bash
# sending a request to a URL passed as an argument, and displaying only the status code of the response
curl -sI -w '%{response_code}' "$1" -o /dev/null
