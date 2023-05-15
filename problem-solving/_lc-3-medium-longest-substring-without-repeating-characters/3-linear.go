"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Complexity
----------
Time: O(n)
Space: O(n)
"""

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func lengthOfLongestSubstring(s string) int {
    seen := make(map[byte]int)
    ans, left, right := 0, 0, 0
    for right < len(s) {
        seen[s[right]] += 1
        for seen[s[right]] > 1 {
            seen[s[left]] -= 1
            left += 1
        }
        ans = max(ans, right - left + 1)
        right += 1
    }
    return ans
}
