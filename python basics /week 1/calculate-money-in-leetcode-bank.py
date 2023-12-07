class Solution:
    def totalMoney(self, n: int) -> int:
        first = [1,3,6,10,15,21,28]
        full = n // 7
        remaining = n % 7
        if full != 0:
            Last_value = 28  + 7 * (full-1 )
            Full_value = full*((28+Last_value)/2)
        else:
            Full_value = 0
        if remaining != 0:
            remain_value = first[remaining-1] + (full)   * (remaining)
            # remain_value = ( full + 1 + (full + 1) * remaining) * remaining / 2
        else:
            remain_value = 0
        return int(Full_value + remain_value) 
        