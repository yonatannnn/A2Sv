class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        def reveal(n):
            revealed_list = list(range(n))
            result = []
            index = 0
            while revealed_list:
                if not index & 1:
                    result.append(revealed_list.pop(0))
                else:
                    revealed_list.append(revealed_list.pop(0))
                index += 1
            return result

        revealed_indices = reveal(len(deck))
        sorted_indices = sorted([value, original_index] for original_index, value in enumerate(revealed_indices))
        deck.sort()
        return [deck[j] for _, j in sorted_indices]
