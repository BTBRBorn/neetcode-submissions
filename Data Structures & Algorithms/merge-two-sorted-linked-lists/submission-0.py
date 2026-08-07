# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            head = list1
            cur_iter = list1
            st_iter = list2
        else:
            head = list2
            cur_iter = list2
            st_iter = list1
        while cur_iter:
            if st_iter.val >= cur_iter.val:
                prev_iter = cur_iter
                cur_iter = cur_iter.next
            else:
                prev_iter.next = st_iter
                prev_iter = st_iter
                st_iter = cur_iter
                cur_iter = prev_iter.next
        prev_iter.next = st_iter
        
        return head
                
                






        

                
        