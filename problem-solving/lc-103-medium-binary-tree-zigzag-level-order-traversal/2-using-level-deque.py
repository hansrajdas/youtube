"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Complexity
----------
Time: O(H*W) -> O(n)
Space: O(H*W) -> O(n)

H = Height of the tree
W = Average width (number of nodes given level) of tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        zigZag = []
        rightToLeft = False
        dq = collections.deque([root])
        while dq:
            level = collections.deque([])
            for _ in range(len(dq)):
                node = dq.popleft()
                if rightToLeft:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            zigZag.append(level)
            rightToLeft = not rightToLeft
        return zigZag
