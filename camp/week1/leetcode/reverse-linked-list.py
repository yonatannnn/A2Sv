# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = []
        if not head:
            return head
        curr = head
        while curr:
            new.append(curr.val)
            curr = curr.next
        new.reverse()
        new_head = ListNode(new[0])
        curr = new_head
        for i in range(1,len(new)):
            curr.next = ListNode(new[i])
            curr = curr.next
        return new_head
        