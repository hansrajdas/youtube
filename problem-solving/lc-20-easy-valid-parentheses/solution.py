"""
https://leetcode.com/problems/valid-parentheses/

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        for i in range(len(s)):
            if s[i] in mapping:
                if not stack or stack.pop() != mapping[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return len(stack) == 0
