"""
https://leetcode.com/problems/symmetric-tree/

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return checkSymmetric(root.left, root.right)

def checkSymmetric(left, right):
    if left is None or right is None:
        return left == right
    if left.val != right.val:
        return False
    return checkSymmetric(left.left, right.right) and checkSymmetric(left.right, right.left)
