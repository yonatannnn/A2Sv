# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        h = []
        curr = head
        while curr:
            h.append(curr.val)
            curr = curr.next
        i = 0
        j = len(h) - 1
        while i < j:
            if h[i] != h[j]:
                return False
            i += 1
            j -= 1
        return True
        