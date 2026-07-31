class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount + 1] * (amount+1)

        for i, e in enumerate(memo):
            if i == 0: 
                memo[i] = 0
                continue
            for c in coins:
                if e - c <= 0: continue
                elif e - c == 1:
                    memo[i] = 1
                else: memo[i] = min(memo[i-c]+1, memo[i])

        return memo[amount] if memo[amount] < amount+1 else -1
                