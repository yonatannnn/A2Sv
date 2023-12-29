class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = Counter(arr1)
        ans = []
        print(n)
        for num in arr2:
            new = [num] * n[num]
            ans.extend(new)
            n.pop(num)
        dicList = list(n.keys())
        dicList.sort()
        nDict = {
            i : n[i] for i in dicList
        }
        for val in nDict:
            new = [val] * n[val]
            ans.extend(new)
            n.pop(val)
        return ans
