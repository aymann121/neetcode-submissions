class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        sol = self.permute(nums[1:])
        res = []
        for e in sol:
            cur = e.copy()
            for i in range(len(e)+1):
                cur.insert(i, nums[0])
                res.append(cur)
                cur = e.copy()
        return res