"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

Complexity
----------
Time: O(n^2)
Space: O(n)

Reference: https://leetcode.com/problems/number-of-longest-increasing-subsequence/solutions/835323/python-3-dp-explanation/

NOTE:
- There is O(nlogn) solution also but solution is hard to understand
- https://github.com/hansrajdas/algorithms/blob/master/Level-3/LIS_O_nlogn.c
- https://leetcode.com/problems/number-of-longest-increasing-subsequence/solutions/916196/python-short-o-n-log-n-solution-beats-100-explained/
"""

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lenLIS = [1] * n
        countLIS = [1] * n
        maxlen = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lenLIS[j] + 1 > lenLIS[i]:
                        lenLIS[i] = lenLIS[j] + 1
                        countLIS[i] = countLIS[j]
                    elif lenLIS[j] + 1 == lenLIS[i]:
                        countLIS[i] += countLIS[j]
            maxlen = max(maxlen, lenLIS[i])

        numLIS = 0
        for i in range(n):
            if lenLIS[i] == maxlen:
                numLIS += countLIS[i]
        return numLIS
