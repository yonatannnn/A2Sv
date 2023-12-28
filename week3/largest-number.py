class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        newList = []
        for num in nums:
            s = str(num)
            newList.append(s)
        for i in range(len(newList)):
            for j in range(i+1,len(newList)):
                if newList[i] + newList[j] > newList[j] + newList[i]:
                    continue
                else:
                    newList[i] , newList[j] = newList[j] , newList[i]
        ans = ''.join(newList)
        if ans[0] == "0":
            return "0"
        return ans
        
                
            
        
        