/*
https://leetcode.com/problems/longest-palindrome/

Complexity
----------
Time: O(n)
Space: O(n)
*/

func longestPalindrome(s string) int {
    mp := make(map[rune]int)
    for _, c := range s {
        mp[c] += 1
    }

    ans, oddCount := 0, false
    for _, v := range mp {
        if v % 2 == 0 {
            ans += v
        } else {
            ans += v - 1
            oddCount = true
        }
    }

    // We can take only one odd number of times occurring char
    if oddCount {
        ans += 1
    }
    return ans
}
