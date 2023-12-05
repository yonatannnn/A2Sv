class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        nums = {}
        z = 0 
        for i in order:
            nums[i] = z
            z += 1
        def check(words,nums,order):
            lw1= len(words[0])
            lw2 = len(words[1])
            maximum = max(lw1,lw2)
            minimum = min(lw1,lw2)
            if len(words[0]) > len(words[1]):
                boo = True
            else:
                boo = False
            for i in range(2):
                for _ in range(maximum - minimum):
                    words[i] += order[0] 
            for i in range(maximum):
                print(words[0][i],words[1][i])
                if nums[words[0][i]] > nums[words[1][i]]:
                    return False
                elif nums[words[0][i]] < nums[words[1][i]]:
                    return True
            if boo:
                return False
            else:
                return True

        i = 0
        while i < len(words) - 1:
            if not check([words[i],words[i+1]],nums,order):
                return False
            i += 1
        return True

        