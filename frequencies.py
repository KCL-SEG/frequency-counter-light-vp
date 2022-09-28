"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(len(items)):
        j = 0;
        currItem = items[i]
        while(currItem == items[i]):
            j = j + 1
            frequencies.update({currItem : j})
        else:
            currItem = items[i]
    return frequencies

print(f' {frequencies( ['a','a'] ) } ')
