"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    if(len(items) != 0):
        for i in items:
            i = str(i)
            if i in frequencies.keys():
                frequencies[i] += 1
            else:
                frequencies[i] = 1
    return frequencies
print(frequencies(['0', 4, 4,'4','d','d','e',0,'a','d','4']))
print(frequencies(['a', 'a', 'b', 'b', 'b', 'c']))
