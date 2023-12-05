class Solution:
    def average(self, salary: List[int]) -> float:
        minval = min(salary)
        maxval = max(salary)
        sumval = minval + maxval
        sum = 0
        for i in range(len(salary)):
            sum = sum + salary[i]
        return (sum - sumval)/(len(salary)-2)
