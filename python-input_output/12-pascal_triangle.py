#!/usr/bin/python3
"""Defines a pascals triangle fucntion"""


def pascal_triangle(n):
    """Reprsent Pascal's Triangle of size n.

    Returns a list of lists of integers reprsenting the triangle.
    """
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles