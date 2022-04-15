#!/usr/bin/python3

"""
Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer. In the case that there are no arguments (or the provided array in compiled languages is empty), return 1.
"""
from math import lcm as lc
def lcm(*nums):
    return lc(*nums)

    
if __name__ == "__main__":
    print(lcm(2,3,4))

