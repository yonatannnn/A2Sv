class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        m = 0
        l = 0
        for i in range(0,len(tasks),4):
            m = max(m,tasks[i]+processorTime[l])
            l += 1
        return m

        