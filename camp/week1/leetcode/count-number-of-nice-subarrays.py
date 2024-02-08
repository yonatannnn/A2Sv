class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = [-1]
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(len(nums))
        i = 1
        j = k
        ans = 0
        print(odd)
        while j < len(odd) - 1:
            val1 = odd[i] - odd[i-1]
            val2 = odd[j+1] - odd[j]
            print(val1 , val2)
            ans += val1 * val2
            i += 1
            j += 1
        return ans
