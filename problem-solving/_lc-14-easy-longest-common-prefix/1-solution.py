"""
https://leetcode.com/problems/longest-common-prefix/

Complexity
----------
Time: O(n)
Space: O(1)
"""

def commonPrefix(s1, s2):
    ans = []
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            break
        ans.append(s1[i])
    return ''.join(ans)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0]
        res = strs[0]
        for i in range(1, len(strs)):
            res = commonPrefix(res, strs[i])
        return res
