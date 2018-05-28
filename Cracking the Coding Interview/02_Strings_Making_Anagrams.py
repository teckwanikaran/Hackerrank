#!/bin/python3
from collections import Counter

def make_anagrams(a, b):
    """
    Input: Counter(a) and Counter(b)
    Output: Sum of different characters
    eg: a = "cde" and b = "abc"
    >>> 4
    """
    
    difference_a_and_b = a - b  # (Counter({'d': 1, 'e': 1})
    difference_b_and_a = b - a  # (Counter({'a': 1, 'b': 1})
    addition = difference_a_and_b + difference_b_and_a  # Counter({'d': 1, 'e': 1, 'a': 1, 'b': 1})
    
    return len(list(addition.elements()))  # list(addition.elements()) =  (['d', 'e', 'a', 'b'])

def main():
    a = Counter(input()) # Counter(a) = (Counter({'c': 1, 'd': 1, 'e': 1})
    b = Counter(input()) # Counter(b) = (Counter({'a': 1, 'b': 1, 'c': 1})
    print (make_anagrams(a, b))
    
if __name__ == '__main__':
    main()
