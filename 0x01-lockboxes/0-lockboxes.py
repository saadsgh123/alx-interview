#!/usr/bin/env python3
"""
module contains a single function that
determines if all the boxes can be opened.
"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    method that determines if all the boxes can be opened.
    :param boxes: boxes to check
    :return: True if all boxes can be opened, else return False
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if new_key < n and not unlocked[new_key]:
                unlocked[new_key] = True
                keys.append(new_key)

    return all(unlocked)
