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


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
