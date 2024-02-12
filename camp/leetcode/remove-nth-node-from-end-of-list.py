# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        node = length - n
        if node == 0:
            temp = head
            head = head.next
            del temp
            return head
        prev = head
        curr = head.next
        while curr and node > 1:
            prev = prev.next
            curr = curr.next
            node -= 1
        print(prev , curr)
        prev.next = curr.next
        return head


        