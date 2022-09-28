"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    j = 0;
    currItem = items[0]
    for i in range(len(items)):
        while(currItem == items[i]):
            j = j + 1
            frequencies.update({currItem : j})
        else:
            currItem = items[i]
            j = 0
    return frequencies
