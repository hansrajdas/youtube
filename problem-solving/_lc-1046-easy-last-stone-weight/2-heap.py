"""
https://leetcode.com/problems/last-stone-weight/

Complexity
----------
Time: (nlogn)
Space: O(logn)  // Don't take any space but recursive calls to build heap will take space
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            w1 = heapq.heappop(stones)
            w2 = heapq.heappop(stones)
            if w1 != w2:
                heapq.heappush(stones, w1 - w2)
        return 0 if len(stones) == 0 else -stones[0]
