class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indices = defaultdict(int)
        for index , value in enumerate(s):
            indices[value] = index
        ans = []
        last = indices[s[0]]
        start = 0
        for i , val in enumerate(s):
            if indices[val] > last:
                last = indices[val]

            if i == last:
                ans.append(i - start + 1)
                start = i + 1
        

            
        return ans


        