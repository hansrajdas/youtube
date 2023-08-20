"""
https://leetcode.com/problems/burst-balloons/

Complexity
----------
Time: O(n^3)
Space: O(n^2)

Reference
---------
Explanation: https://leetcode.com/problems/burst-balloons/solutions/892552/for-those-who-are-not-able-to-understand-any-solution-with-diagram/
Code: https://leetcode.com/problems/burst-balloons/solutions/76228/share-some-analysis-and-explanations/
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]  # To handle edge cases
        cache = {}
        def coins(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            cache[(l, r)] = 0
            for m in range(l + 1, r):
                cache[(l, r)] = max(
                    cache[(l, r)],
                    nums[l]*nums[m]*nums[r] + coins(l, m) + coins(m, r))
            return cache[(l, r)]
        return coins(0, len(nums) - 1)
