/*
https://leetcode.com/problems/longest-substring-without-repeating-characters

Complexity
----------
Time: O(n)
Space: O(n)

Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/1729/11-line-simple-java-solution-o-n-with-explanation/
*/

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
        if v, ok := seen[s[right]]; ok {
            // For input "pwwkew" we has to make left = 2 (not 1) from 0
            left = max(left, v + 1)
        }
        seen[s[right]] = right
        ans = max(ans, right - left + 1)
        right += 1
    }
    return ans
}
