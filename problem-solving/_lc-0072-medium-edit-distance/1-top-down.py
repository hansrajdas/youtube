"""
https://leetcode.com/problems/edit-distance/

Complexity
----------
Time: O(m*n)
Space: O(m*n)

m and n are lengths of 2 strings.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def distance(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in cache:
                return cache[(i, j)]
            if word1[i] == word2[j]:
                cache[(i, j)] = distance(i + 1, j + 1)
            else:
                cache[(i, j)] = 1 + min(
                    distance(i + 1, j),     # Delete
                    distance(i, j + 1),     # Insert
                    distance(i + 1, j + 1)  # Replace
                    )
            return cache[(i, j)]
        return distance(0, 0)
