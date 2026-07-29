# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def reverse(node):
            p1 = None
            p2 = node
            
            while p2:
                temp = p2.next
                p2.next = p1
                p1 = p2
                p2 = temp
            return p1


        def merge(node1, node2):
            head = node1
            p1 = node1
            p2 = node2
            while p1 and p2:
                temp = p1.next
                temp2 = p2.next
                p1.next = p2
                p2.next = temp

                p2 = temp2
                p1 = temp
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        list2 = reverse(second)
        h = merge(head, list2)
        # print(list2.val, h.val)