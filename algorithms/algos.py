"""
This source code contains basic algorithms which I wrote myself in Python to better understand and apply these algorithms.
"""
                
def bin_search(ordered_list,target):
    min,max = 0, len(ordered_list)
    while min<=max:
        mid = int((min+max) / 2)
        val = ordered_list[mid]
        if val == target:
            return mid
        elif val < target:
            min = mid +1
        else:
            max = max -1
        
    raise ValueError("The target value is not in the list")


if __name__ == "__main__":
    a = Graph({"a":["b"]})