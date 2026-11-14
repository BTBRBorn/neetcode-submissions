# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge(self, list1, list2):
        merged = ListNode(-1)
        head = merged
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

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                if i+1 != len(lists):
                    merged = self.merge(lists[i], lists[i+1])
                else:
                    merged = self.merge(lists[i], None)
                temp.append(merged)
            lists = temp
        if lists:
            return lists[0]
        return None
