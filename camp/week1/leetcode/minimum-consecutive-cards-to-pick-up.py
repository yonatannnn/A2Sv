from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        right = 0
        ans = float('inf')
        while right < len(cards):
            count[cards[right]] += 1
            if count[cards[right]] == 2:
                while count[cards[right]] == 2:
                    count[cards[left]] -= 1
                    left += 1
                print(right , left)
                ans = min(ans , right - left + 2)
            right += 1
        return ans if ans <= 10 ** 5 else -1

