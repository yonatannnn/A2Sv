class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pMap = [0] * 26
        sMap = [0] * 26
        for i in range(len(p)-1,-1,-1):
            pMap[ord(p[i])-97] += 1
            sMap[ord(s[i])-97] += 1
        ans = [0] if pMap == sMap else []
        for i in range(len(p),len(s)):
            sMap[ord(s[i])-97] += 1
            if sMap[ord(s[i-len(p)])-97] != 0:
                sMap[ord(s[i-len(p)])-97] -= 1
            if sMap == pMap:
                ans.append(i-len(p)+1)
        return ans
                

        
        