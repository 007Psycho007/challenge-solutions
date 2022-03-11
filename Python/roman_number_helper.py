""" 
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
"""
class RomanNumerals:
    roman_numerals = {
                    "IV":  	4,
                    "IX":	9,
                    "I":	1,
                    "V":	5,
                    "XC":	90,
    	            "XL":	40,
                    "X":	10,
                    "L":	50,
                    "CM":	900,
                    "CD":	400,               
                    "C":	100,
                    "D":	500,                   
                    "M":	1000,
    }
    @classmethod
    def to_roman(cls,mval):
        temp_roman_numerals = dict(sorted(cls.roman_numerals.items(),reverse=True, key=lambda x:x[1]))
        roman=""
        while mval>0:
            for key,value in temp_roman_numerals.items():
                if mval >= value:
                    roman = roman + (key * int(mval / value))
                    mval = mval % value
        return roman
    @classmethod
    def from_roman(cls,roman_num):
        result= 0
        for key,value in cls.roman_numerals.items():
            if roman_num.count(key) > 0:
                result += roman_num.count(key) * value
                roman_num = roman_num.replace(key,"")
        return result
                
if __name__ == "__main__":
    r = RomanNumerals()
    print(r.to_roman(1795))
    print(r.from_roman("MDCCXCV"))