class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return head
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
