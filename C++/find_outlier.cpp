/*
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
*/

int FindOutlier(std::vector<int> arr)
{
    int odd;
    int even;
    int odd_count = 0;
    int even_count = 0;
    for (int i=0;i< arr.size();i++)
      if (arr[i] % 2 == 0) {
        even_count += 1;
        even = arr[i];
      } else {
        odd_count += 1;
        odd = arr[i];
      }
    if (even_count == 1) {
      return even;
    } else {
      return odd;
    }
}