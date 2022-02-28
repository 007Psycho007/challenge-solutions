"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def split_strings(s):
    if len(s) % 2 == 1:
        s += "_"
    o = []
    while s:
        
        o.append(s[:2])
        s = s[2:]
    return o