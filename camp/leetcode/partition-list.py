# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
 
        lessHead = ListNode()
        less = lessHead

        greaterHead = ListNode()
        greater = greaterHead

        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = curr
            else:
                greater.next = curr
                greater = curr
            curr = curr.next
        
        less.next = greaterHead.next
        greater.next = None
        
        return lessHead.next
        
                

        