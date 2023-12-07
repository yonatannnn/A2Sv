class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indexes = []
        j = 1
        for i in range(len(boxes)):
            indexes.append(0)
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    indexes[i] += abs(j-i)
        return indexes