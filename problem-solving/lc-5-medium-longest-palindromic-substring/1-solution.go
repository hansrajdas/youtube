/*
https://leetcode.com/problems/longest-palindromic-substring/

Complexity
----------
Time: O(n^2)
Space: O(1)
*/

func isPalindrome(s string, l, r, start, end int) (int, int) {
    for l >= 0 && r < len(s) && s[l] == s[r] {
        if end - start < r - l {
            start, end = l, r
        }
        l -= 1
        r += 1
    }
    return start, end
}

func longestPalindrome(s string) string {
    start, end := 0, 0
    n := len(s)
    for i := 0; i < n; i++ {
        // Odd len palindrome - having center char at i
        start, end = isPalindrome(s, i - 1, i + 1, start, end)

        // Even len palindrome - don't have center char
        start, end = isPalindrome(s, i, i + 1, start, end)
    }
    return s[start:end + 1]
}
