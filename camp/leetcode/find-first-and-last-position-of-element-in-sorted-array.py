class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                ans = max(mid , ans)
                low = mid + 1
        if ans == -1:
            return [-1 , -1]
        last = ans

        low = 0
        high = len(nums) - 1
        ans = float('inf')
        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                ans = min(mid , ans)
                high = mid - 1
        return [ans , last]


        


