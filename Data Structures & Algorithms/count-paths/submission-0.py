class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for i in range(m)]

        def helper(i,j):
            if i >= m or j >= n: return 0 
            if dp[i][j] != -1: return dp[i][j]
            if i == m-1 and j == n-1: return 1

            dp[i][j] = helper(i+1,j) + helper(i,j+1)

            return dp[i][j]

        return helper(0,0)