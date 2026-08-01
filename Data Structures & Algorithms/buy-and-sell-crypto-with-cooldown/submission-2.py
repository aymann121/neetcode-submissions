class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = [[-1]*len(prices), [-1]*len(prices)]
        
        def dfs(buy, i):
            if i >= len(prices): return 0
            if buy and memo[0][i] != -1: return memo[0][i]
            if not buy and memo[1][i] != -1: return memo[1][i]

            if buy:
                memo[0][i] = max(0, dfs(False, i+1) - prices[i], dfs(True, i+1))
                return memo[0][i]
            else:
                memo[1][i] = max(0, dfs(True, i+2) + prices[i], dfs(False, i+1))
                return memo[1][i]

        return dfs(True, 0)