class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def findRow(row , last):
            print(last , row)
            if row == rowIndex:
                return last
            curr = [1]
            for i in range(len(last) - 1):
                curr.append(last[i] + last[i+1])
            curr.append(1)
            return findRow(row + 1 , curr)

        return findRow(0 , [1])
            



        