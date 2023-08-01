"""
https://leetcode.com/problems/sum-of-left-leaves/description/

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
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isLeftChild=False) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val if isLeftChild else 0
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)
