"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1:

9 ==> -1
111 ==> -1
531 ==> -1
"""
from itertools import permutations
def next_bigger(n):
    combs = sorted([int(''.join(i)) for i in permutations([i for i in str(n)])])
    res = []
    [res.append(x) for x in combs if x not in res]
    if res[-1] == n:
        return -1
    return combs[combs.index(n)+1]


if __name__ == "__main__":
    print(next_bigger(414))

