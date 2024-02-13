# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        i = 0
        ans = 0
        while curr:
            ans *= 2
            ans += curr.val
            curr = curr.next
        return ans

        