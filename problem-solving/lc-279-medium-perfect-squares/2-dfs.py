"""
https://leetcode.com/problems/perfect-squares/

Complexity
----------
Time: O(n*sqrt(n))
Space: O(n)
"""

def getPerfectSquares(n):
    perfectSquares = []
    x = 1
    while x * x <= n:
        perfectSquares.append(x * x)
        x += 1
    return perfectSquares

class Solution:
    def numSquares(self, n: int) -> int:
        perfectSquares = getPerfectSquares(n)
        visited = set()
        dq = collections.deque([n])
        res = 0
        while dq:
            count = len(dq)
            while count > 0:
                count -= 1
                element = dq.popleft()
                for x in perfectSquares:
                    if element == 0:
                        return res
                    if element - x < 0:
                        break
                    if element - x not in visited:
                        visited.add(element - x)
                        dq.append(element - x)
            res += 1
        return -1
