""" 
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""
def scramble(s1, s2):
    for char in s2:
        if char in s1:
            s1.replace(char, "", 1)
        else:
            return False
    return True

print(scramble("Hello","elli"))