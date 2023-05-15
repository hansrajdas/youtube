/*
https://leetcode.com/problems/power-of-two/

Complexity
----------
Time: O(1)
*/

func isPowerOfTwo(n int) bool {
    return n != 0 && n & (n - 1) == 0
}
