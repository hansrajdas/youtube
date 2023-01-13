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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        dq = collections.deque([(root, False)])
        res = 0
        while dq:
            node, isLeftChild = dq.popleft()
            if node.left is None and node.right is None:
                res += (node.val if isLeftChild else 0)
            if node.left:
                dq.append((node.left, True))
            if node.right:
                dq.append((node.right, False))
        return res
