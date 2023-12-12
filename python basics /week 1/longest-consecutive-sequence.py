from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Dict = Counter(nums)
        maximum = 0
        if len(nums) > 0:
            maximum = 1
        for key in Dict:
            count = 0
            if key - 1 not in Dict:
                while key in Dict:
                    count += 1
                    key += 1
                if maximum < count:
                    maximum = count
        return maximum
        