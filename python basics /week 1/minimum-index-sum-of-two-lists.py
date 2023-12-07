class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        i = 0
        Dict = {}
        minimum = float('inf')
        for i in range(len(list1)):
            word = list1[i]
            for j in range(len(list2)):
                if list2[j] == word:
                    if i + j < minimum:
                        minimum = i + j
                        Dict[minimum] = [word]                       
                    elif i + j == minimum:
                        Dict[minimum].append(word)
                    else:
                        continue
        print(Dict)
        return [] if 2000 < minimum else Dict[minimum]
