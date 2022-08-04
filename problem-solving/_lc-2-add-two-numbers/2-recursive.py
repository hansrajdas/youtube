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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], c=0) -> Optional[ListNode]:
        val = c
        if l1 != None:
            val += l1.val
            l1 = l1.next
        else:
            l1 = None
        if l2 != None:
            val += l2.val
            l2 = l2.next
        else:
            l2 = None
        node = ListNode(val % 10)
        c = val // 10
        if l1 or l2 or c:
            node.next = self.addTwoNumbers(l1, l2, c)
        return node
