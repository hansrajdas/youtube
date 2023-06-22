/*
https://leetcode.com/problems/palindromic-substrings/

Complexity
----------
Time: O(n^2)
Space: O(1)
*/

func countPalindrome(s string, left, right int) int {
    count := 0
    for left >= 0 && right < len(s) && s[left] == s[right] {
        left -= 1
        right += 1
        count += 1
    }
    return count
}

func countSubstrings(s string) int {
    count := len(s)
    for mid := 0; mid < len(s); mid++ {
        count += countPalindrome(s, mid - 1, mid + 1)
        count += countPalindrome(s, mid, mid + 1)
    }
    return count
}
