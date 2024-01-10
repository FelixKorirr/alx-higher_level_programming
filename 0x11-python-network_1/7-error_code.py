#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    url = argv[1]

    response = get(url)
    ERROR_TXT = 'Error code: {}'
    status = response.status_code
    print(ERROR_TXT.format(status) if (status >= 400) else response.text)
