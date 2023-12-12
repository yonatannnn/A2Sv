class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.pairs = {}
        for i in range(n+1):
            self.pairs[i] = 0
        self.pointer = 1
        
    def insert(self, idKey: int, value: str) -> List[str]:
        self.pairs[idKey] = value
        ans = []
        while self.pointer <= self.n and self.pairs[self.pointer]:
            ans.append(self.pairs[self.pointer])
            self.pointer += 1
        return ans
        




# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)