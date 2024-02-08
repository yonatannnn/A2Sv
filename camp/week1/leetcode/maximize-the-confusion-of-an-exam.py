from collections import defaultdict
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = {
            'T' : 0,
            'F' : 0
        }
        i = 0
        j = 0
        ans = 0
        while j < len(answerKey):
            if min(count.values()) <= k:
                count[answerKey[j]] += 1
                j += 1
            else:
                ans = max(ans , sum(count.values()) - 1)
                count[answerKey[i]] -= 1
                i += 1
        if min(count.values()) <= k:
            ans = max(ans , sum(count.values()))
        else:
            ans = max(ans , sum(count.values()) - 1)

        return ans
        
        
            

        