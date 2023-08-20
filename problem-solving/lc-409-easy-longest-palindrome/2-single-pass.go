/*
https://leetcode.com/problems/longest-palindrome/

Complexity
----------
Time: O(n)
Space: O(n)
*/

type void struct{}

func longestPalindrome(s string) int {
    var nullVal void
    set := make(map[rune]void)
    for _, c := range s {
        if _, ok := set[c]; ok {
            delete(set, c)
        } else {
            set[c] = nullVal
        }
    }
    if len(set) > 0 {
        return len(s) - len(set) + 1
    }
    return len(s)
}
