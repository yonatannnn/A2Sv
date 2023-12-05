class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        amount = capacity
        step = 1
        for i in range(len(plants)-1):
            amount -= plants[i]
            step += 1
            if amount < plants[i+1]:
                step += 2 * (i + 1)
                amount = capacity
        return step
        