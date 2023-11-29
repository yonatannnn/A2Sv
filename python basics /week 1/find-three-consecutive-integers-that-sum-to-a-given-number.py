class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        z = num / 3
        if z == int(z):
            return [int(z-1),int(z),int(z+1)]
        return []