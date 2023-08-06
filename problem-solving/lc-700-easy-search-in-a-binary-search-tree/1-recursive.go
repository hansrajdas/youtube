/*
https://leetcode.com/problems/search-in-a-binary-search-tree/

Complexity
----------
Time: O(n)
Space: O(n)
*/

 /**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func searchBST(root *TreeNode, val int) *TreeNode {
    if root == nil {
        return nil
    }
    if root.Val == val {
        return root
    } else if root.Val < val {
        return searchBST(root.Right, val)
    } else {
        return searchBST(root.Left, val)
    }
}