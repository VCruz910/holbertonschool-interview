#!/usr/bin/python3
"""
Interview Practice
"""


from itertools import dropwhile


def canUnlockAll(boxes):
    """
    Method that determines
    if all boxes can be 
    opened.
    """

    """ Variables: """
    BoxKeys = {0}
    BoxRange = range(len(boxes))

    while True:
        NotFound = set()

        for I in BoxRange:
            if I in BoxKeys:
                for BoxKey in dropwhile(lambda K: K in BoxKeys, boxes[I]):
                    BoxKeys.add(BoxKey)
            else:
                NotFound.add(I)

        if BoxRange == NotFound:
            return False

        if not NotFound:
            return True

        BoxRange = NotFound
