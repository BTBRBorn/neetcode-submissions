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
            higher = list2
        else:
            head = list2
            cur_iter = list2
            higher = list1
        while cur_iter:
            if higher.val >= cur_iter.val:
                prev_iter = cur_iter
                cur_iter = cur_iter.next
            else:
                prev_iter.next = higher
                prev_iter = higher
                higher = cur_iter
                cur_iter = prev_iter.next
        prev_iter.next = higher

        return head
