class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        size = 0
        length = len(tickets)
        while tickets[k] != 0:
            if tickets[i] != 0:
                size += 1
                tickets[i] -= 1
            if i == length - 1:
                i = 0
            else:
                i += 1
        return size
