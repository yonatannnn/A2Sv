class FrequencyTracker:

    def __init__(self):
        self.dic=defaultdict(int)
        self.dic2=defaultdict(int)

    def add(self, number: int) -> None:
        self.dic[number]+=1
        self.dic2[self.dic[number]] += 1
        if self.dic2[self.dic[number]-1]:
            self.dic2[self.dic[number]-1] -= 1
        if self.dic2[self.dic[number]-1]==0:
            del self.dic2[self.dic[number]-1]

    def deleteOne(self, number: int) -> None:        
        if self.dic[number]:
            self.dic2[self.dic[number]] -= 1
            if self.dic2[self.dic[number]]==0:
                del self.dic2[self.dic[number]]
            self.dic[number] -= 1
            self.dic2[self.dic[number]] += 1
        
    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.dic2
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)