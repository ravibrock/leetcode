class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        def reversal(nums):
            if nums: return ListNode(nums.pop(-1), reversal(nums))
        
        return reversal(nums)
