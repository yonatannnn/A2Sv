# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        c = []
        while curr:
            c.append(curr.val)
            curr = curr.next
        dif = right - left
        a = c[:left-1]
        b = c[left-1:right]
        e = c[right:]
        b.reverse()
        new = a + b + e
        h = ListNode()
        res = h
        for i in new:
            res.next = ListNode(i)
            res = res.next
        return h.next



        