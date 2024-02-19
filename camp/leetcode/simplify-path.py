class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted_path = path.split("/")
        canonical_path = []
        allowed = set(["","..","."])
        for directory in splitted_path:
            if canonical_path and directory == '..':
                canonical_path.pop()
            else:
                if directory not in allowed:
                    canonical_path.append(directory)
        s = "/" + "/".join(canonical_path)
        return s 
                    