class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        if len(nums) == 0: return True
        half = sum(nums) / 2

        cur = []
        curSum = 0
        def helper(i):
            nonlocal curSum
            if i >= len(nums): return False
            if curSum == half: return True
            if curSum > half: return False
            cur.append(nums[i])
            curSum += nums[i]
            valid = helper(i+1)
            cur.pop()
            curSum -= nums[i]
            return valid or helper(i+1)

        return helper(0)


        