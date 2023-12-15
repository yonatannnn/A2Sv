class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = {}
        for whole in cpdomains:
            visited = whole.split()
            j = len(visited[1]) - 1
            ans = ""
            while j > -1:
                if visited[1][j] == ".":
                    counter[ans] = counter.get(ans,0) + int(visited[0])
                ans = visited[1][j] + ans
                j -= 1
            counter[ans] = int(visited[0]) + counter.get(ans,0)
        answer = []
        for key in counter:
            answer.append(f'{counter[key]} {key}')
        return answer


        