"""
https://leetcode.com/problems/minimum-falling-path-sum/

Complexity
----------
Time: O(n*n)
Space: O(1)
"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for r in range(1, n):
            for c in range(n):
                if c == 0:
                    matrix[r][c] += min(matrix[r - 1][c],
                                        matrix[r - 1][c + 1])
                elif c == n - 1:
                    matrix[r][c] += min(matrix[r - 1][c],
                                        matrix[r - 1][c - 1])
                else:
                    matrix[r][c] += min(matrix[r - 1][c],
                                        matrix[r - 1][c - 1],
                                        matrix[r - 1][c + 1])
        return min(matrix[n - 1])
