/*
https://leetcode.com/problems/guess-number-higher-or-lower-ii/

Complexity
----------
Time: O(n^3)
Space: O(n^2)
*/

func getMoneyAmount(n int) int {
    var (
        dp [][]int
        temp int
    )
    for i := 0; i < n + 1; i++ {
        dp = append(dp, make([]int, n + 1))
    }

    // This loop in run in reverse order because in the recurrence relation,
    // we are accessing future index (g + 1) of l.
    for l := n - 1; l > 0; l-- {
        for h := l + 1; h <= n; h++ {
            dp[l][h] = math.MaxInt32
            for g := l; g < h; g++ {
                temp = g + max(dp[l][g - 1], dp[g + 1][h])
                dp[l][h] = min(dp[l][h], temp)
            }
        }
    }
    return dp[1][n]
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
