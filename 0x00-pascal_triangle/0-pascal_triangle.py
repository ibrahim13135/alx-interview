#!/usr/bin/python3

def generate_pascal_triangle(num_rows: int) -> list:
    """
    Generate a Pascal's Triangle with a specified number of rows.

    Args:
        num_rows (int): The number of rows in the triangle.

    Returns:
        list: A list of lists, where each sublist represents a row in the triangle.
    """
    triangle = []

    for n in range(num_rows):
        row = [1] * (n + 1)

        if n != 0:
            for i in range(1, n):
                row[i] = triangle[n - 1][i - 1] + triangle[n - 1][i]

        triangle.append(row)

    return triangle
