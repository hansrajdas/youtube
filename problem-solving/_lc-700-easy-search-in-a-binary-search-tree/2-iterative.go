/*
https://leetcode.com/problems/search-in-a-binary-search-tree/

Complexity
----------
Time: O(n)
Space: O(1)
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
    node := root
    for node != nil {
        if node.Val == val {
            return node
        } else if node.Val < val {
            node = node.Right
        } else {
            node = node.Left
        }
    }
    return nil
}
