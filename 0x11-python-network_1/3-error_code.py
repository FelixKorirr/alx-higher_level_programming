#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""

if __name__ == '__main__':
    import sys
    from urllib import request, error

    argv = sys.argv
    url = argv[1]
    try:
        with request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.status))
