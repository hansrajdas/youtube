/*
https://leetcode.com/problems/longest-palindromic-substring/

Complexity
----------
Time: O(n^2)
Space: O(1)
*/

func longestPalindrome(s string) string {
    start, end := 0, 0
    n := len(s)
    for i := 0; i < n; i++ {
        // Odd len palindrome - having center char
        l := i - 1
        r := i + 1
        for l >= 0 && r < n && s[l] == s[r] {
            if end - start < r - l {
                start, end = l, r
            }
            l -= 1
            r += 1
        }
        // Even len palindrome - don't have center char
        l = i
        r = i + 1
        for l >= 0 && r < n && s[l] == s[r] {
            if end - start < r - l {
                start, end = l, r
            }
            l -= 1
            r += 1
        }
    }
    return s[start:end + 1]
}
