#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    a = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=a)
    print(res.json().get("id"))
