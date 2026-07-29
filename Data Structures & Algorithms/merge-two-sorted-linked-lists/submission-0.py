# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        p1 = list1
        p2 = list2
        if p1.val > p2.val:
            p1, p2 = list2, list1
        head = p1
        
        while p2:
            if not p1.next:
                p1.next = p2
                break
            elif p2.val < p1.next.val:
                temp = p1.next
                p1.next = p2
                p2 = p2.next
                p1.next.next = temp
                p1 = p1.next
            else:
                p1 = p1.next
        return head