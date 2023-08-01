/*
https://leetcode.com/problems/power-of-two/

Complexity
----------
Time: O(logn)
*/

func isPowerOfTwo(n int) bool {
    if n < 1 {
        return false
    }
    for n % 2 != 1 {
        n /= 2
    }
    return n == 1
}
