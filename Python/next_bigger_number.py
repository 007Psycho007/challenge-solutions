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

"""
This implementation is too slow since it has to calculate every possible combination and they can get quite big.
from itertools import permutations
    combs = sorted([int(''.join(i)) for i in permutations([i for i in str(n)])])
    res = []
    [res.append(x) for x in combs if x not in res]
    print(res)
    if res[-1] == n:
        return -1
    return res[res.index(n)+1]
"""



def next_bigger(h):
   
    arr = [int(i) for i in str(h)]
      # find the length of the array
    n = len(arr)
     
    # start from the right most digit and find the first
    # digit that is smaller than the digit next to it.
    k = n - 2
    while k >= 0:
        if arr[k] < arr[k + 1]:
            break
        k -= 1
         
    # reverse the list if the digit that is smaller than the
    # digit next to it is not found.
    if k < 0:
        arr = arr[::-1]
    else:
       
          # find the first greatest element than arr[k] from the
        # end of the list
        for l in range(n - 1, k, -1):
            if arr[l] > arr[k]:
                break
 
        # swap the elements at arr[k] and arr[l     
        arr[l], arr[k] = arr[k], arr[l]
         
        # reverse the list from k + 1 to the end to find the
        # most nearest greater number to the given input number
        arr[k + 1:] = reversed(arr[k + 1:])
     
        r = int(''.join([str(i) for i in arr]))
        if r == h: 
            return -1
        else:
            return r
    return -1 
# Driver code

if __name__ == "__main__":
    print(nextPermutation(59884848459853)) # 59884848483559

