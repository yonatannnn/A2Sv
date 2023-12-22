# Keep track of the largest bit that is on

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        dict = {
            i : 1 for i in range(len(flips))
        }
        count = 0
        zero = 0
        one = float('-inf')
        for i in flips:
            value = i - 1
            if value > one:
                one = value
            dict.pop(value)
            for key in dict:
                zero = key
                break
            if zero == one + 1:
                count += 1
        count += 1
        return count
