/*
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps

Complexity
----------
Time: O(S*min(S, N))
Space: O(S*min(S, N))

S = Steps
N = arrLen
*/

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func numWays(steps int, arrLen int) int {
    M := 1000000007
    var dp [][]int
    maxPos := min(steps, arrLen)
    for i := 0; i < steps + 1; i++ {
        dp = append(dp, make([]int, maxPos))
    }
    dp[0][0] = 1
    for s := 1; s <= steps; s++ {
        for i := 0; i < maxPos; i++ {
            dp[s][i] = dp[s - 1][i]
            if i > 0 {
                dp[s][i] = (dp[s][i] + dp[s - 1][i - 1]) % M
            }
            if i < maxPos - 1 {
                dp[s][i] = (dp[s][i] + dp[s - 1][i + 1]) % M
            }
        }
    }
    return dp[steps][0]
}
