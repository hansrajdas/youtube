/*
https://leetcode.com/problems/reverse-linked-list/

Complexity
----------
Time: O(n)
Space: O(1)
*/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    curr := head
    next := head
    for curr != nil {
        next = next.Next
        curr.Next = prev
        prev = curr
        curr = next
    }
    return prev
}
