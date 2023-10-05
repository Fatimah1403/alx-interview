#!/usr/bin/python3
"""A python module that determines if all boxes can be opened
   from a list of lists
"""


def canUnlockAll(boxes):
    """A function that returns True of all box in
    boxes can be opend
    """
    if not boxes:
        return False
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        box_id = unseen_boxes.pop()
        if not box_id or box_id < 0 or box_id >= n:
            continue
        if box_id not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box_id])
            seen_boxes.add(box_id)
    return n == len(seen_boxes)
