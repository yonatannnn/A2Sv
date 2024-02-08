# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        answer =  ans
        sett = set()
        curr = head
        while curr:
            sett.add(curr.val)
            curr = curr.next
        li = list(sett)
        li.sort(reverse = False)
        for i in li:
            ans.next = ListNode(i)
            ans = ans.next
        return answer.next
        