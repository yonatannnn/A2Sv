class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        leftSum = 0
        rightSum = sum(nums)
        n = len(nums)
        rightSize = n - 1
        for i in range(n):
            rightSum -= nums[i]
            
            value1 = i * nums[i] - leftSum
            value2 = rightSum - rightSize * nums[i]
            value = value1 + value2

            ans.append(value)

            leftSum += nums[i]
            rightSize -= 1
        return ans

        