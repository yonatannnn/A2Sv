class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            for j in range(1,len(heights)-i):
                if heights[j-1] < heights[j]:
                    heights[j-1] , heights[j] = heights[j] , heights[j-1]
                    names[j-1] , names[j] = names[j] , names[j-1]
        print(heights)
        return names