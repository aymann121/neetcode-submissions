class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return True
        if sum(nums) % 2: return False

        target = sum(nums) // 2
        dp = [False for i in range(target + 1)]
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j-num] or dp[j]
        return dp[target]


        