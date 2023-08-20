"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level_order = []
        node = root
        dq = collections.deque([root])
        while dq:
            level = []
            for _ in range(len(dq)):
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level_order.append(level)
        return level_order
