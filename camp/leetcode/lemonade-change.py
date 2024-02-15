class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = 0
        notes = {
            5 : 0,
            10 : 0,
            20 : 0
        }
        for i in bills:
            if i == 5:
               notes[5] += 1
            elif i == 10 and notes[5]:
                notes[5] -= 1
                notes[10] += 1
            elif i == 20 and ((notes[10] and notes[5]) or (notes[5] > 2)):
                if notes[10] and notes[5]:
                    notes[10] -= 1
                    notes[5] -= 1
                else:
                    notes[5] -= 3
                notes[20] += 1
            else:
                return False
        return True
                    