# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        target, end = head, head

        while end:
            if n < 0: target = target.next
            end = end.next
            n -= 1
        
        if n == 0: return head.next
        target.next = target.next.next if target.next else target.next

        return head
