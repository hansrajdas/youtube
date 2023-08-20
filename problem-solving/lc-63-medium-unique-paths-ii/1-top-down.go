/*
https://leetcode.com/problems/unique-paths-ii

Complexity
----------
Time: O(rows*cols)
Space: O(rows*cols)
*/

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    rows := len(obstacleGrid)
    cols := len(obstacleGrid[0])
    cache := make(map[string]int)
    var P func(int, int) int  // This declaration is requried.
    P = func(r, c int) int {
        if r < 0 || r >= rows || c < 0 || c >= cols || obstacleGrid[r][c] == 1 {
            return 0
        }
        if r == rows - 1 && c == cols - 1 {
            return 1
        }
        key := fmt.Sprintf("%d-%d", r, c)
        if v, ok := cache[key]; ok {
            return v
        }
        cache[key] = P(r + 1, c) + P(r, c + 1)
        return cache[key]
    }
    return P(0, 0)
}
