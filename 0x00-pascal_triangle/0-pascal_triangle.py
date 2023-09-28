#!/usr/bin/python3
"""
A function that returns  a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """function that create the pascal triangle"""
    if n <= 0:
        return []
    # Lets loop through n
    triangle = []
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)
    # print(triangle)
    return triangle
