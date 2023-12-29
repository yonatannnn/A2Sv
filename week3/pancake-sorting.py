class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        if len(arr) == 2:
            if arr == sorted(arr):
                return []
            else:
                return [2]
        def flip(arr,k):
            a = arr[:k+1]
            b = arr[k+1:]
            return a[::-1] + b
        val = []
        for i in arr:
            if i not in val:
                val.append(i)
        ans = []
        i = 1
        while arr != sorted(arr) and len(arr) - 1 > 1:
            m = max(val)
            a = arr.index(m)
            ans.append(a+1)
            arr = flip(arr,a)
            arr = flip(arr,len(arr)-i)
            val.pop(val.index(m))
            ans.append(len(arr)-i+1)
            i += 1
        return ans

            
        