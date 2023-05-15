/*
https://leetcode.com/problems/search-a-2d-matrix/

Complexity
----------
Time: O(log(rows*cols)
Space: O(1)
*/

func searchMatrix(matrix [][]int, target int) bool {
    rows := len(matrix)
    cols := len(matrix[0])
    left := 0
    right := rows * cols - 1
    for left <= right {
        mid := (left + right) / 2
        r := mid / cols
        c := mid % cols
        if matrix[r][c] == target {
            return true
        } else if matrix[r][c] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return false
}
