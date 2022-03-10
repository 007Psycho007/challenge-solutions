""" 
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""
def solution(args):
    curr_range=[]
    range_string = []
    for num in args:
        if len(curr_range) == 0:
            curr_range.append(num)
        elif curr_range[-1] == num -1:
            curr_range.append(num)
        else:
            print(curr_range)
            if len(curr_range) == 1:
                range_string.append(f"{curr_range[0]}")
            elif len(curr_range) == 2:
                range_string.append(f"{curr_range[0]},{curr_range[-1]}")
            else:
                range_string.append(f"{curr_range[0]}-{curr_range[-1]}")
            curr_range = [num]
    if len(curr_range) != 0:
        print(curr_range)
        if len(curr_range) == 1:
            range_string.append(f"{curr_range[0]}")
        elif len(curr_range) == 2:
            range_string.append(f"{curr_range[0]},{curr_range[-1]}")
        else:
            range_string.append(f"{curr_range[0]}-{curr_range[-1]}")
        curr_range = [num]
    return ",".join(range_string)