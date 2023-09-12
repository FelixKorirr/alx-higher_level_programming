#!/usr/bin/python3
"""Reads from standard input and computes metrics"""


def print_stats(size, status_codes):
    """Print accumulated metrics"""

    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    j = ['200', '301', '400', '401', '403', '404', '405', '500']
    i = 0

    try:
        for h in sys.stdin:
            if i == 10:
                print_stats(size, status_codes)
                i = 1
            else:
                i += 1

            h = h.split()

            try:
                size += int(h[-1])
            except (IndexError, ValueError):
                pass

            try:
                if h[-2] in j:
                    if status_codes.get(h[-2], -1) == -1:
                        status_codes[h[-2]] = 1
                    else:
                        status_codes[h[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
