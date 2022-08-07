"""
https://leetcode.com/problems/validate-binary-search-tree/

Complexity
----------
Time: O(N)
Space: O(N)
"""

class Solution:
    def helper(self, root, mn, mx):
        if root is None:
            return True
        if root.val <= mn or root.val >= mx:
            return False
        return (self.helper(root.left, mn, root.val) and
                self.helper(root.right, root.val, mx))
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -sys.maxsize, sys.maxsize)
