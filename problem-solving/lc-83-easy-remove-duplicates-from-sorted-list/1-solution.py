"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Complexity
----------
Time: O(n)
Space: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p:
            curr = p
            p = p.next
            while p and curr.val == p.val:
                p = p.next
            curr.next = p
        return head
