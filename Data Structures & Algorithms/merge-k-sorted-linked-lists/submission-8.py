# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for ll in lists:
            while ll:
                vals.append(ll.val)
                ll = ll.next
        if not vals:
            return None
        vals.sort()
        merged = ListNode()
        tail = merged
        for i in range(len(vals)):
            merged.val = vals[i]
            if i != len(vals) -1:
                merged.next = ListNode()
                merged = merged.next
        return tail
        
