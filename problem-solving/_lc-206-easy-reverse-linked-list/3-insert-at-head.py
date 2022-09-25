"""
https://leetcode.com/problems/reverse-linked-list/

Complexity
----------
Time: O(n)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        p = head
        while p is not None:
            node = p
            p = p.next
            node.next = newHead
            newHead = node
        return newHead
