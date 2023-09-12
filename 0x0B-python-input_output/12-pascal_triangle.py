#!/usr/bin/python3
"""Defines pascal_triangle function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n"""
    if n <= 0:
        return []

    x = [[1]]
    while len(x) != n:
        tri = x[-1]
        y = [1]
        for i in range(len(tri) - 1):
            y.append(tri[i] + tri[i + 1])
        y.append(1)
        x.append(y)
    return x
