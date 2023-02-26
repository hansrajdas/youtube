"""
https://leetcode.com/problems/combination-sum-iv

Complexity
----------
Time: O(n*T)
Space: O(T + n*T) = O(n*T)  // First T for cache size, then n*T for recursion stack

n = len(nums)
T = target
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {0: 1}  # This initialization will avoid writing base case of `if tg == 0: return 1`
        def _combinationSum4(tg):
            if tg in cache:
                return cache[tg]
            count = 0
            for n in nums:
                if n <= tg:
                    count += _combinationSum4(tg - n)
            cache[tg] = count
            return count
        return _combinationSum4(target)
