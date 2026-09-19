# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeLists(self, list1: ListNode, list2: ListNode):
        dummy = ListNode()
        merged = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
        if list1:
            merged.next = list1
        if list2:
            merged.next = list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        merged = []
        while len(lists) != 1:
            for i in range(0, len(lists), 2):
                l1 = lists[i]  
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.mergeLists(l1, l2))
            lists = merged[:]
            merged.clear()
        return lists[0]
        