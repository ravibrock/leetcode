# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        tracker = []
        while head.next:
            if head.next in tracker: return True
            else: tracker.append(head.next)
            head = head.next
        return False
