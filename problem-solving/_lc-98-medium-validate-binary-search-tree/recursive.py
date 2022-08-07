"""
https://leetcode.com/problems/validate-binary-search-tree/

Complexity
----------
Time: O(N)
Space: O(N)
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, mn, mx):
            if root is None:
                return True
            if root.val <= mn or root.val >= mx:
                return False
            return (helper(root.left, mn, root.val) and
                    helper(root.right, root.val, mx))

        return helper(root, -sys.maxsize, sys.maxsize)
