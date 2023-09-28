# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [l for l in lists if l]
        if len(lists) == 0: return ListNode().next

        last = combined = lists[0]
        vals = []
        
        for entry in lists[1:]:
            if last:
                while last.next:
                    vals.append(last.val)
                    last = last.next
                last.next = entry
        
        while last:
            vals.append(last.val)
            last = last.next
        
        vals = sorted(vals)
        i = 0

        temp = combined
        while temp:
            temp.val = vals[i]
            temp = temp.next
            i += 1
        
        return combined
