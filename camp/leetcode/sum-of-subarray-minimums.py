class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n 
        right = [n] * n
        stack = []

        for idx, val in enumerate(arr):
            while stack and arr[stack[-1]] >= val:  
                stack.pop()  
            if stack:
                left[idx] = stack[-1]  
            stack.append(idx) 

        stack = [] 
        for idx in range(n - 1, -1, -1):  
            while stack and arr[stack[-1]] > arr[idx]: 
                stack.pop()  
            if stack:
                right[idx] = stack[-1]  
            stack.append(idx) 
        mod = 10**9 + 7 
        result = sum((idx - left[idx]) * (right[idx] - idx) * val for idx, val in enumerate(arr)) % mod
        return result 
