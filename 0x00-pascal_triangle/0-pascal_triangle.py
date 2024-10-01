#!/usr/bin/python3
def pascal_triangle(n):
    result = []  # This will store the final list of lists (rows of Pascal's triangle)

    # Base case: if n is 0, return an empty list
    if n <= 0:
        return result

    # Generate Pascal's Triangle row by row
    for row in range(n):
        child_list = [1] * (row + 1)  # Start each row with 1's

        # Fill the middle values by adding the two numbers from the previous row
        for i in range(1, row):
            child_list[i] = result[row - 1][i - 1] + result[row - 1][i]

        result.append(child_list)  # Append the current row to the result list

    return result
