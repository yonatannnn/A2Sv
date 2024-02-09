class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        value_indices = {}
        for i, num in enumerate(nums):
            if num in value_indices:
                value_indices[num].append(i)
            else:
                value_indices[num] = [i]
        print(value_indices)
        answer = [0] * len(nums)
        for num in value_indices:
            if len(value_indices[num]) != 1:
                leftSum = 0
                rightSum = sum(value_indices[num])
                n = len(value_indices[num])
                rightSize = n - 1
                for i in range(n):
                    rightSum -= value_indices[num][i]
                    
                    value1 = i * value_indices[num][i] - leftSum
                    value2 = rightSum - rightSize * value_indices[num][i]
                    value = value1 + value2

                    answer[value_indices[num][i]] += value

                    leftSum += value_indices[num][i]
                    rightSize -= 1
        return answer
                
