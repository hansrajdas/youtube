/*
https://leetcode.com/problems/longest-common-subsequence/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
*/

func longestCommonSubsequence(text1 string, text2 string) int {
    cache := make(map[string]int)
    var F func(int, int) int
    F = func(i, j int) int {
        if i == len(text1) || j == len(text2) {
            return 0
        }
        key := fmt.Sprintf("%d-%d", i, j)
        if v, ok := cache[key]; ok {
            return v
        }
        if text1[i] == text2[j] {
            cache[key] = 1 + F(i + 1, j + 1)
        } else {
            cache[key] = max(F(i + 1, j), F(i, j + 1))
        }
        return cache[key]
    }
    return F(0, 0)
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
