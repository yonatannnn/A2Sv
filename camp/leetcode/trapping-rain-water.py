class Solution:
    def trap(self, height: List[int]) -> int:
        left_maximum = [0]
        right_maximum = [0]
        for i in range(len(height)):
            left_maximum.append(max(left_maximum[-1] , height[i]))
        for i in range(len(height)-1 , -1 , -1):
            right_maximum.append(max(right_maximum[-1] , height[i]))
        right_maximum.reverse()
        ans = 0
        for i in range(len(left_maximum)-1):
            value = min(left_maximum[i] , right_maximum[i]) - height[i]
            if value > 0:
                ans += value
        return ans
        