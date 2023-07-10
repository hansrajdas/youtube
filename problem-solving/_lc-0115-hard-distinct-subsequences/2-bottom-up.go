/*
https://leetcode.com/problems/distinct-subsequences/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
*/

func numDistinct(s string, t string) int {
    m, n := len(s), len(t)
    var dp [][]int

    for i := 0; i < m + 1; i++ {
        dp = append(dp, make([]int, n + 1))
    }

    for i := 0; i < m + 1; i++ {
        dp[i][0] = 1
    }

    for i := 1; i < m + 1; i++ {
        for j := 1; j < n + 1; j++ {
            if s[i - 1] == t[j - 1] {
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            } else {
                dp[i][j] = dp[i - 1][j]
            }
        }
    }
    return dp[m][n]
}
