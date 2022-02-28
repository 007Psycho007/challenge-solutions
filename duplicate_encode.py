"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Source: codewars.com
"""

def duplicate_encode(word):
    single = []
    duplicate = []
    for letter in word.lower():
        if letter in single:
            duplicate.append(letter)
        else:
            single.append(letter)
    result= ""
    for letter in word.lower():
        if letter in duplicate:
            result += ")"
        else:
            result += "("
    return result
