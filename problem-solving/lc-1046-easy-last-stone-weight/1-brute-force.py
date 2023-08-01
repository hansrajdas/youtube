"""
https://leetcode.com/problems/last-stone-weight/

Complexity
----------
Time: (n*nlogn)
Space: Depends on sorting algorithm
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            w1 = stones.pop()
            w2 = stones.pop()
            diff = abs(w1 - w2)
            if diff:
                stones.append(diff)
                stones.sort()
        return 0 if len(stones) == 0 else stones[0]
