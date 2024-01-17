class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre = [0] * (n + 1)
        for book in bookings:
            pre[book[0]-1] += book[2]
            pre[book[1]] -= book[2]
        ans = [pre[0]]
        for i in range(1 , len(pre)-1):
            ans.append(ans[-1] + pre[i])
        return ans

        

        