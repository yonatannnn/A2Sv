class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		pref , ans, curr= 0,0,0
		dict ={0:1}
		for n in nums:
			curr += n
			diff =  curr -k
			ans += dict.get(diff,0)
			dict[curr] = 1 + dict.get(curr ,0)
		return ans