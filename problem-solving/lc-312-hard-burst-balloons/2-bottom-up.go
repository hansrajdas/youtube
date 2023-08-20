/*
https://leetcode.com/problems/burst-balloons/

Complexity
----------
Time: O(n^3)
Space: O(n^2)

Reference
---------
Explanation: https://leetcode.com/problems/burst-balloons/solutions/892552/for-those-who-are-not-able-to-understand-any-solution-with-diagram/
Code: https://leetcode.com/problems/burst-balloons/solutions/76228/share-some-analysis-and-explanations/
*/

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func maxCoins(nums []int) int {
    N := make([]int, len(nums) + 2)
    copy(N[1:], nums)
    n := len(N)
    N[0], N[n - 1] = 1, 1

    var dp [][]int
    for i := 0; i < n; i++ {
        dp = append(dp, make([]int, n))
    }

    for k := 2; k < n; k++ {
        for l := 0; l < n - k; l++ {
            r := l + k
            for m := l + 1; m < r; m++ {
                dp[l][r] = max(
                    dp[l][r],
                    N[l]*N[m]*N[r] + dp[l][m] + dp[m][r])
            }
        }
    }
    return dp[0][len(N) - 1]
}
