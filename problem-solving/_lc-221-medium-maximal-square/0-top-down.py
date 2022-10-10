"""
https://leetcode.com/problems/maximal-square/

Complexity
----------
Time: O(mn)
Space: O(mn)
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        maxlen = 0
        memo = {}
        def helper(row, col):
            if 0 > row or row >= rows or 0 > col or col >= cols:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            if matrix[row][col] == '1':
                memo[(row, col)] = min(
                    helper(row, col + 1),
                    helper(row + 1, col + 1),
                    helper(row + 1, col)) + 1
                return memo[(row, col)]
            return 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    maxlen = max(maxlen, helper(r, c))
        return maxlen * maxlen
