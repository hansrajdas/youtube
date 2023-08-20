"""
https://leetcode.com/problems/validate-binary-search-tree/

Complexity
----------
Time: O(N)
Space: O(N)
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, mn, mx):
            if root is None:
                return True
            if root.val <= mn or root.val >= mx:
                return False
            return (validate(root.left, mn, root.val) and
                    validate(root.right, root.val, mx))

        return validate(root, -math.inf, math.inf)
