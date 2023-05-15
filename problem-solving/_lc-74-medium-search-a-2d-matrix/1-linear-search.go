/*
https://leetcode.com/problems/search-a-2d-matrix/

Complexity
----------
Time: O(rows + cols)
Space: O(1)
*/

func searchMatrix(matrix [][]int, target int) bool {
    r := 0
    c := len(matrix[0]) - 1
    for r < len(matrix) && c >= 0 {
        if matrix[r][c] == target {
            return true
        } else if matrix[r][c] < target {
            r += 1
        } else {
            c -= 1
        }
    }
    return false
}
