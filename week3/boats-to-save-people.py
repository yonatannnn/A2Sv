class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        r = len(people) - 1
        count = 0
        while i <= r:
            toFind = limit - people[r]
            r -= 1
            count += 1
            if i <= r and people[i] <= toFind:
                i += 1
            
        return count
            

        