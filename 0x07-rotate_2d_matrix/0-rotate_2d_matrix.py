#!/usr/bin/python3
"""n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """matrix, rotate it 90 degrees clockwise"""
    if not matrix:
        return None
    cp_matrix = matrix.copy()
    matrix.clear()

    cp_matrix.reverse()

    for i in range(len(cp_matrix)):
        temp_row = [elem[i] for elem in cp_matrix]
        matrix.append(temp_row)
