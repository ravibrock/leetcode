# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp, length = head, 0
        while temp:
            length += 1
            temp = temp.next
        
        lists = [ListNode() for _ in range(k)]
        p_list = [lists[n] for n in range(k)]
        
        for n in range(k):
            for j in range(length // k + (1 if n < length % k else 0)):
                p_list[n].next = ListNode(head.val)
                p_list[n] = p_list[n].next
                head = head.next
        
        for n in range(len(lists)): lists[n] = lists[n].next

        return lists
        
