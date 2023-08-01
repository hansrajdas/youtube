"""
https://leetcode.com/problems/construct-quad-tree/

Complexity
----------
Time: O(n^2)
Space: O(logn)  // We are dividing by n by half in every call.

Reference: https://leetcode.com/problems/construct-quad-tree/solutions/154565/java-recursive-solution/
"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def qTree(r, c, n):
            """(r, c) is coordinates of top left."""
            if n == 1:
                return Node(grid[r][c] != 0, True, None, None, None, None)
            h = n // 2
            newNode = Node()
            topLeft = qTree(r, c, h)
            topRight = qTree(r, c + h, h)
            bottomLeft = qTree(r + h, c, h)
            bottomRight = qTree(r + h, c + h, h)
            children = [topLeft, topRight, bottomLeft, bottomRight]
            # All are leaf and have same val
            if all(x.isLeaf and x.val == topLeft.val for x in children):
                newNode.val = topLeft.val
                newNode.isLeaf = True
            else:
                newNode.topLeft = topLeft
                newNode.topRight = topRight
                newNode.bottomLeft = bottomLeft
                newNode.bottomRight = bottomRight
                # newNode.val can be True or False
            return newNode
        return qTree(0, 0, len(grid))
