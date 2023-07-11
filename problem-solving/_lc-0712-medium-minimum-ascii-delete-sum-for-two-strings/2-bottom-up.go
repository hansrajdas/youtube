/*
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
*/

func minimumDeleteSum(s1 string, s2 string) int {
    var dp [][]int
    m, n := len(s1), len(s2)
    for i := 0; i < m + 1; i++ {
        dp = append(dp, make([]int, n + 1))
    }
    for i := 1; i < m + 1; i++ {
        dp[i][0] = dp[i - 1][0] + int(s1[i - 1])
    }
    for j := 1; j < n + 1; j++ {
        dp[0][j] = dp[0][j - 1] + int(s2[j - 1])
    }
    for i := 1; i < m + 1; i++ {
        for j := 1; j < n + 1; j++ {
            if s1[i - 1] == s2[j - 1] {
                dp[i][j] = dp[i - 1][j - 1]
            } else {
                dp[i][j] = min(
                    int(s1[i - 1]) + dp[i - 1][j],
                    int(s2[j - 1]) + dp[i][j - 1])
            }
        }
    }
    return dp[m][n]
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
