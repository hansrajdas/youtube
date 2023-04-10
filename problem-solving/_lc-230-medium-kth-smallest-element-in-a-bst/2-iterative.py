"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Complexity
----------
Time: O(n)
Space: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if k == 1:
                return node.val
            k -= 1
            node = node.right
        return -1  # Should not reach here as `1 <= k <= n`
