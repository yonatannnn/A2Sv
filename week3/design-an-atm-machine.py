class ATM:
    def __init__(self):
        self.d = [0] * 5
        self.value = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        self.d = [a + b for a, b in zip(self.d, banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        pre = [0] * 5
        for i in range(4, -1, -1):
            pre[i] = min(self.d[i], amount // self.value[i])
            amount -= pre[i] * self.value[i]    
            if not amount: break
        else:        
            return [-1]    
        self.d = [a - b for a, b in zip(self.d, pre)]
        return pre