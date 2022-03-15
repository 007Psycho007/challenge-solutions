/* 
This source code contains basic algorithms which I wrote myself in C++ to better understand and apply these algorithms.
*/

#include <iostream>
#include <vector>

int bin_search(std::vector<int> arr,int target) {
    bool loop = true;
    int min = 0;
    int max = arr.size();
    int mid;
    while (min<=max) {
        mid = (min + max) / 2;

        if (arr[mid] == target) {
            return mid;
        }
        else if (arr[mid] < target)
        {   
            min = mid + 1;
        } else {
            max = mid - 1;
        }
    }
    return -1 ;
} 
