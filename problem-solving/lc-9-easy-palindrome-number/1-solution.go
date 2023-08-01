/*
https://leetcode.com/problems/palindrome-number/

Complexity
----------
Time: O(logn)  // Base 10
Space: O(1)
*/

func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }
    var rev int
    n := x
    for n > 0 {
        d := n % 10
        n = n / 10
        rev = (rev << 3) + (rev << 1) + d  // rev = rev * 10 + d
    }
    return x == rev
}
