/*
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps

Complexity
----------
Time: O(S*min(S, N))
Space: O(min(S, N))

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
    maxPos := min(steps, arrLen)
    dp := make([]int, maxPos)
    dp[0] = 1
    for s := 1; s <= steps; s++ {  // or s = [0, steps - 1]
        temp := make([]int, maxPos)
        for i := 0; i < maxPos; i++ {
            temp[i] = dp[i]
            if i > 0 {
                temp[i] = (temp[i] + dp[i - 1]) % M
            }
            if i < maxPos - 1 {
                temp[i] = (temp[i] + dp[i + 1]) % M
            }
        }
        dp = temp
    }
    return dp[0]
}
