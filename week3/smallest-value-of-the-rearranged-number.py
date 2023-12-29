class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        strn = str(num)
        negative = False
        li = []
        minimum = float('inf')
        maximum = float('-inf')
        for i in strn:
            if i == "-":
                negative = True
            else:
                li.append(int(i))
                if int(i) != 0:
                    minimum = min(int(i),minimum)
                    maximum = max(int(i),maximum)

        if not negative:
            li.remove(minimum)
            li.sort()
            minimum = str(minimum)
            ans = f'{minimum}'
            for i in range(len(li)):
                ans += str(li[i])
        else:
            li.remove(maximum)
            li.sort(reverse = True)
            maximum = str(maximum)
            ans = f'-{maximum}'
            for i in range(len(li)):
                ans += str(li[i])
        return int(ans)