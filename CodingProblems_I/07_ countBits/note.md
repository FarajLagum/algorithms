338. Counting Bits
Easy
Topics
Companies
Hint
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105


Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?






In binary operations, the shift left (`<<`) and shift right (`>>`) operators are used to move the bits of a binary number to the left or right respectively.

- **Shift Left (`<<`)**: A left binary shift removes the leftmost bit (often called the most significant bit) and adds a 0 to the right end of the number³. This operation effectively multiplies the number by 2. For example, if we have the binary number `1100` (which is 12 in decimal), and we shift it left by 1 bit, we get `11000`, which is 24 in decimal¹.

- **Shift Right (`>>`)**: A right binary shift removes the rightmost bit (often called the least significant bit) and adds a 0 to the left end of the number³. This operation effectively divides the number by 2. For example, if we have the binary number `1100` (which is 12 in decimal), and we shift it right by 1 bit, we get `110`, which is 6 in decimal¹.

It's important to note that these operations can change the value of the binary number by a power of two³. Also, the exact behavior of the right shift operator can depend on the language and whether the number is signed or unsigned². In some languages, a right shift on a signed number will keep the sign bit (the leftmost bit) the same, effectively performing an arithmetic shift¹.


