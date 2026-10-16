class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        nums.sort()
        def backtrack(i, tar):
            if tar < 0 or i == len(nums):
                return
            if tar == 0:
                res.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i, tar-nums[i])
            cur.pop()
            backtrack(i+1, tar)

        backtrack(0, target)
        return res
