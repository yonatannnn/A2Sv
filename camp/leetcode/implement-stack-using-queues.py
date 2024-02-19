class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.count = 0

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.count += 1

    def pop(self) -> int:
        print(self.queue1)
        self.queue1 , self.queue2 = self.queue2 , self.queue1
        self.queue2.reverse()
        val = self.queue2.pop(0)
        if self.queue2:
            self.queue2.reverse()
        self.queue1 , self.queue2 = self.queue2 , self.queue1
        self.count -= 1
        print(self.queue1)
        return val

    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        return not self.count
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()