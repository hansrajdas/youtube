"""
https://leetcode.com/problems/reverse-linked-list/

Complexity
----------
Time and space: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, curr):
            if curr is None:
                return prev
            newHead = reverse(curr, curr.next)
            curr.next = prev
            return newHead
        return reverse(None, head)
