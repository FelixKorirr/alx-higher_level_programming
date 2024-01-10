#!/usr/bin/python3
"""Script that fetches an URL with requests package."""
import requests


if __name__ == "__main__":
    x = requests.get('https://alx-intranet.hbtn.io/status')
    y = x.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(y), y))
