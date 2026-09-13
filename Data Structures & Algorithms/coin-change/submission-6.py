class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(curAmount):
            if curAmount in memo:
                return memo[curAmount]
            if curAmount < 0:
                return -1
            if curAmount == 0:
                return 0
            minCoins = float('infinity')
            for c in coins:
                val = dfs(curAmount-c)
                if val == -1:
                    continue
                minCoins = min(minCoins, 1 + val)
            memo[curAmount] = minCoins
            return minCoins
        res = dfs(amount)
        if res == float('infinity'):
            return -1
        return res