"""
https://leetcode.com/problems/add-two-numbers/

Complexity
----------
O(max(m, n)) time and space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = 0
        head = ListNode(-1)
        p = head
        while p1 or p2 or carry:
            val = carry
            if p1 is not None:
                val += p1.val
                p1 = p1.next
            if p2 is not None:
                val += p2.val
                p2 = p2.next
            p.next = ListNode(val % 10)
            p = p.next
            carry = val // 10
        return head.next
