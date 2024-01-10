#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter
as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    lettr = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": lettr}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
