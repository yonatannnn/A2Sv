class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        rlt = {}
        for files in paths:
            dirFil = files.split(" ")
            Dir = dirFil[0]
            File = dirFil[1:]
            for f in File:
                nm_cont = f.split("(")
                name = nm_cont[0]
                content = nm_cont[1]
                if content in rlt:
                    rlt[content].append(Dir +"/"+name)
                else:
                    rlt[content] = [Dir+"/"+name]
        ans = []
        for key in rlt:
            if len(rlt[key]) > 1:
                ans.append(rlt[key])
        return ans
            

        
        