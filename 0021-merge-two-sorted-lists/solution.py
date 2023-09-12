# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return list1
        leader = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                leader.next = ListNode()
                leader.val = list1.val
                leader, list1 = leader.next, list1.next
            else:
                leader.next = ListNode()
                leader.val = list2.val
                leader, list2 = leader.next, list2.next
       
        leader.val = list1.val if list1 else list2.val
        leader.next = list1.next if list1 else list2.next

        return head
