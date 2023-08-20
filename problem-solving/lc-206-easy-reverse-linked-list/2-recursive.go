/*
https://leetcode.com/problems/reverse-linked-list/

Complexity
----------
Time and space: O(n)
*/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverse(prev, curr *ListNode) *ListNode {
    if curr == nil {
        return prev
    }
    newHead := reverse(curr, curr.Next)
    curr.Next = prev
    return newHead
}

func reverseList(head *ListNode) *ListNode {
    return reverse(nil, head)    
}
