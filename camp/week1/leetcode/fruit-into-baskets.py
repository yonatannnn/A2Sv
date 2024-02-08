class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dicts = {}
        i = 0
        j = 0
        maximum = 0
        while j < len(fruits):
            if len(dicts) <= 2:
                maximum = max(maximum,sum(dicts.values()))
                dicts[fruits[j]] = 1 + dicts.get(fruits[j],0)
                j += 1
            else:
                dicts[fruits[i]] -= 1
                if dicts[fruits[i]] == 0:
                    dicts.pop(fruits[i])
                i += 1
        if len(dicts) <= 2:
            maximum = max(maximum,sum(dicts.values()))
        return maximum

            

        