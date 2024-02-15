class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = 0
        curr = headA
        while curr:
            lengthA += 1
            curr = curr.next
        lengthB = 0
        curr = headB
        while curr:
            lengthB += 1
            curr = curr.next
        dif = abs(lengthA - lengthB)
        if lengthA > lengthB:
            pointerA = headA
            while dif > 0:
                pointerA = pointerA.next
                dif -= 1
            pointerB = headB

            while pointerA != pointerB and pointerA and pointerB:
                pointerA = pointerA.next
                pointerB = pointerB.next
            return pointerA
        else:
            pointerB = headB
            while dif > 0:
                pointerB = pointerB.next
                dif -= 1
            pointerA = headA

            while pointerA != pointerB and pointerA and pointerB:
                pointerA = pointerA.next
                pointerB = pointerB.next
            return pointerB



