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
        self.k = k
        def inorder(root):
            if root is None:
                return None
            val = inorder(root.left)
            if val is not None:
                return val
            if self.k == 1:
                return root.val
            self.k -= 1
            return inorder(root.right)
        return inorder(root)
