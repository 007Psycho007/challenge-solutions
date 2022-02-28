/*
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
*/

unsigned int countBits(unsigned long long n){
  int bin[100];
  int count {0};
  int i {0};
  // I can convert a decimal number to a binary by dividing 
  // the number by 2 and assigning the Rest of that division as the left most number and do that until no number is left.
  while (n > 0) {
    bin[i] = n % 2;
    n = n / 2;
    i++;
  }
  for (int j = i - 1; j >= 0; j--) {
   if (bin[j] == 1) {
       count++;
   }
  }

  return count;
}