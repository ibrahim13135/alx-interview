#!/usr/bin/python3
"""
This module contains a function to determine if all the boxes can be opened.

The function canUnlockAll checks if all the boxes in a list of lists can be
unlocked
using the keys available in the boxes. Each box may contain keys to other boxes

Usage Example:
    canUnlockAll([[1], [2], [3], [4], []])  # Returns: True
    canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]])
    canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists where each sublist contains
        keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if key < n:
                    stack.append(key)

    return len(visited) == n
