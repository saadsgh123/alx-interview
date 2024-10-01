#!/usr/bin/python3
"""Triangle Triangle"""


def pascal_triangle(n):
    """ pascal_triangle function """
    result = []
    if n <= 0:
        return result

    for row in range(n):
        child_list = [1] * (row + 1)

        for i in range(1, row):
            child_list[i] = result[row - 1][i - 1] + result[row - 1][i]

        result.append(child_list)

    return result
