class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N_count = [0]
        n = len(customers)
        for customer in customers:
            if customer == "N":
                N_count.append(N_count[-1] + 1)
            else:
                N_count.append(N_count[-1])
        
        minimum_penality = N_count[-1]
        index = n
        accumulator_y = 0
        for i in range(n - 1, -1, -1):
            if customers[i] == "Y":
                accumulator_y += 1
            current_penality = N_count[i] + accumulator_y
            if current_penality <= minimum_penality:
                minimum_penality = current_penality
                index = i
        
        return index

            