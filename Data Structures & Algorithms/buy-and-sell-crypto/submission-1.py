class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, p2 = 0, 0
        maxProfit = 0

        while p2 < len(prices):
            maxProfit = max(maxProfit, prices[p2] - prices[p1])
            p2 += 1
            if p2 < len(prices) and prices[p1] > prices[p2]:
                p1 = p2
        return maxProfit