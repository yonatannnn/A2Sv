# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        c = []
        while curr:
            c.append(curr.val)
            curr = curr.next
        c.pop(len(c)-n)
        h = ListNode()
        res = h
        for i in c:
            res.next = ListNode(i)
            res = res.next
        return h.next
            
        