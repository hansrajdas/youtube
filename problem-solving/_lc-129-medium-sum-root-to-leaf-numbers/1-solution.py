"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/

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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def _sumNumbers(root, currNum):
            if root is None:
                return 0
            currNum = (currNum << 3) + (currNum << 1) + root.val
            if root.left is None and root.right is None:
                return currNum
            return _sumNumbers(root.left, currNum) + _sumNumbers(root.right, currNum)
        return _sumNumbers(root, 0)
