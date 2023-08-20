/*
https://leetcode.com/problems/longest-palindromic-subsequence/

Complexity
----------
Time: O(n^2)
Space: O(n^2)

Another approach
----------------
Reverse given string and find LCS b/w given string and reversed: https://leetcode.com/problems/longest-palindromic-subsequence/solutions/99151/super-simple-solution-using-reversed-string/
*/

func longestPalindromeSubseq(s string) int {
    n := len(s)
    var dp [][]int

    for i := 0; i < n; i++ {
        dp = append(dp, make([]int, n))
    }

    for i:= n - 1; i >=0; i-- {
        dp[i][i] = 1
        for j := i + 1; j < n; j++ {
            if s[i] == s[j] {
                dp[i][j] = 2 + dp[i + 1][j - 1]
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            }
        }
    }
    return dp[0][n - 1]
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
