"""
This kata is the performance version of Don't give me five by user5036852.

Your mission, should you accept it, is to return the count of all integers in a given range which do not contain the digit 5 (in base 10 representation).
You are given the start and the end of the integer range. The start and the end are both inclusive.

Examples:

1,9 -> 1,2,3,4,6,7,8,9 -> return 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> return 12
The result may contain fives. ;-)
The start will always be smaller than the end. Both numbers can be also negative.

The regions can be very large and there will be a large number of test cases. So brute force solutions will certainly time out!

Good luck, warrior!
"""
# Invalid Solution for Codewars: Execution with large Lists takes too long
def dont_give_me_five(start: int,end: int) -> int:
    return len([ x for x in range(start,end+1) if x % 5 != 0])


def main():
    print(dont_give_me_five(1, 9))
if __name__ == "__main__":
    main()
