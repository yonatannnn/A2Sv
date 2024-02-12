class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0   

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        else:
            curr = self.head
            while index > 0:
                curr = curr.next
                index -= 1
            return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        if index <= self.length and index > -1:
            if index == 0:
                self.addAtHead(val)
            else:
                curr = self.head
                while index > 1:
                    curr = curr.next
                    index -= 1
                newNode.next = curr.next
                curr.next = newNode
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.length and index > -1:
            if index == 0:
                dummy = self.head
                self.head = self.head.next
                del dummy
            else:
                prev = self.head
                curr = prev.next
                while index > 1:
                    prev = prev.next
                    curr = curr.next
                    index -= 1
                prev.next = curr.next
            self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)