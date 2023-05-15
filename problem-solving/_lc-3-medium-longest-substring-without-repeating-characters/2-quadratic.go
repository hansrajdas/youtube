"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Complexity
----------
Time: O(n^2)
Space: O(n)
"""

type void struct{}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func lengthOfLongestSubstring(s string) int {
    var null void
    ans := 0
    n := len(s)
    for i := 0; i < n; i++ {
        set := make(map[byte]void)
        for j := i; j < n; j++ {
            set[s[j]] = null
            if len(set) < j - i + 1 {
                break
            }
            ans = max(ans, len(set))
        }
    }
    return ans
}
