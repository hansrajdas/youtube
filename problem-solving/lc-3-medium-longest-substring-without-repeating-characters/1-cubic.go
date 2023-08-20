/*
https://leetcode.com/problems/longest-substring-without-repeating-characters

Complexity
----------
Time: O(n^3)
Space: O(n)

NOTE: This solution is not accepted, gives TLE
*/

type void struct{}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func allUniq(start, end int, s string) bool {
    set := make(map[byte]void)
    var null void
    for i := start; i < end + 1; i++ {
        if _, ok := set[s[i]]; ok {
            return false
        }
        set[s[i]] = null
    }
    return true
}

func lengthOfLongestSubstring(s string) int {
    ans := 0
    n := len(s)
    for i := 0; i < n; i++ {
        for j := i; j < n; j++ {
            if allUniq(i, j, s) {
                ans = max(ans, j - i + 1)
            }
        }
    }
    return ans
}
