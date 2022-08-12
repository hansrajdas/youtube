"""
https://leetcode.com/problems/plus-one/

Complexity
----------
Time: O(n)
Space: (1)
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):  # n - 1 to 0
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
