# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None
        curr = head
        while curr:
            next = curr.next
            curr.next = reversed
            reversed = curr
            curr = next
        return reversed
            

        