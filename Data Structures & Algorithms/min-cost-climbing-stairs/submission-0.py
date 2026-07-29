class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1, p2 = cost[-1], 0
        for i in range(len(cost)-2,-1, -1):
            temp = p1
            p1 = min(p1, p2) + cost[i]
            p2 = temp
        return min(p1, p2)