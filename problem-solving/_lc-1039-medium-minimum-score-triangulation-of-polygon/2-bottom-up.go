/*
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

Complexity
----------
Time: O(N^3)
Space: O(N^2)

Reference: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/solutions/294265/python-in-depth-explanation-dp-for-beginners/
*/

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func minScoreTriangulation(values []int) int {
    n := len(values)
    var dp [][]int

    for i := 0; i < n; i++ {
        dp = append(dp, make([]int, n))
    }

    for l := 2; l < n; l++ {
        for left := 0; left < n - l; left++ {
            right := left + l
            dp[left][right] = math.MaxInt32
            for mid := left + 1; mid < right; mid++ {
                dp[left][right] = min(
                    dp[left][right],
                    values[left]*values[mid]*values[right] + dp[left][mid] + dp[mid][right])
            }
        }
    }
    return dp[0][n - 1]
}
