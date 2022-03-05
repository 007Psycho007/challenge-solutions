"""
Write a function that 
takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed 
(Just like the name of this Kata). Strings passed in will consist of only letters and spaces. 
paces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => 
returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
    """

# We can do this in one by using a list comprehension in which we split the string into a list and reverse the string
# on a condition. We can directly join this list back to a string in the same line.
def spin_words(sentence):
    return " ".join([ w if len(w)<5 else w[::-1] for w in sentence.split(" ")])

