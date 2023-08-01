/*
https://leetcode.com/problems/longest-common-subsequence/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
*/

func longestCommonSubsequence(text1 string, text2 string) int {
    var dp [][]int
    m, n := len(text1), len(text2)
    for i := 0; i < m + 1; i++ {
        dp = append(dp, make([]int, n + 1))
    }
    for i := 1; i < m + 1; i++ {
        for j :=1; j < n + 1; j++ {
            if text1[i - 1] == text2[j - 1] {
                dp[i][j] = 1 + dp[i - 1][j - 1]
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            }
        }
    }
    return dp[m][n]
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
