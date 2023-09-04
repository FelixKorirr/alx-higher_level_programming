#!/usr/bin/python3
"""Solves the nqueens puzzle"""
import sys


def _init_board(n):
    """Initialize chessboard with 0's"""
    x = []
    [x.append([]) for j in range(n)]
    [y.append(' ') for j in range(n) for y in x]
    return (x)


def ret_deepcopy(x):
    """Return a deepcopy of a chessboard."""
    if isinstance(x, list):
        return list(map(ret_deepcopy, x))
    return (x)

def ret_list(x):
    """Returns list of lists representation of chessboard."""
    s = []
    for p in range(len(x)):
        for q in range(len(x)):
            if x[p][q] == "Q":
                s.append([p, q])
                break
    return (s)


def x_out(x, y, z):
    """X spots on a chessboard"""

    for c in range(z + 1, len(x)):
        x[y][c] = "x"

    for c in range(z - 1, -1, -1):
        x[y][c] = "x"

    for r in range(y + 1, len(x)):
        x[r][z] = "x"

    for r in range(y - 1, -1, -1):
        x[r][z] = "x"

    c = z + 1
    for r in range(y + 1, len(x)):
        if c >= len(x):
            break
        x[r][c] = "x"
        c += 1

    c = z - 1
    for r in range(y - 1, -1, -1):
        if c < 0:
            break
        x[r][c]
        c -= 1

    c = z + 1
    for r in range(y - 1, -1, -1):
        if c >= len(x):
            break
        x[r][c] = "x"
        c += 1

    c = z - 1
    for r in range(y + 1, len(x)):
        if c < 0:
            break
        x[r][c] = "x"
        c -= 1
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    x = _init_board(int(sys.argv[1]))
    s = recursive_solve(x, 0, 0, [])
    for i in s:
        print(i)
