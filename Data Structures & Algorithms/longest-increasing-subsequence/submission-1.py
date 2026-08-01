class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        memo = [1] * len(nums)
        res = 1

        for i, e in enumerate(nums):
            memoVal = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    memoVal = max(memoVal, memo[j] + 1)
            memo[i] = memoVal
            res = max(memoVal, res)
        return res
    


                        


