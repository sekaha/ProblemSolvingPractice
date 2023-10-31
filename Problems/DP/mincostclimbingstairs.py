from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_costs = [0]*(len(cost)-2)+cost[-2:]

        for i in range(len(cost)-3,-1,-1):
            total_costs[i] = min(total_costs[i+1],total_costs[i+2])+cost[i]
            
        return min(total_costs[:2])

sol = Solution()
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))