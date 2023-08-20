/*
https://leetcode.com/problems/unique-paths-ii

Complexity
----------
Time: O(rows*cols)
Space: O(rows*cols)

NOTE: This can also be solved with O(1) space by utilising input matrix instead of dp table.
*/

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    rows := len(obstacleGrid)
    cols := len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1 {
        return 0
    }
    var dp [][]int
    for i := 0; i < rows; i++ {
        dp = append(dp, make([]int, cols))
    }
    dp[0][0] = 1
    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if obstacleGrid[r][c] == 0 {
                if r > 0 {
                    dp[r][c] += dp[r - 1][c]
                }
                if c > 0 {
                    dp[r][c] += dp[r][c - 1]
                }
            }
        }
    }
    return dp[rows - 1][cols - 1]
}
