"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

import re

def to_camel_case(text: str) -> str:
    # I use a Regex-Expression to Split the String either a "_" or a "-"
    text_split = re.split(r'_|-',text)
    for i in range(len(text_split)):
        # If its not the first word I captilize the first letter of each word
        if i != 0:
            text_split[i]=text_split[i].capitalize()
    return "".join(text_split)