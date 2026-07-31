class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        def helper(i,j):
            p1, p2 = nums[i], max(nums[i], nums[i+1])
            i += 1
            while i+1 <= j:
                temp = p2
                p2 = max(p2, p1 + nums[i+1])
                p1 = temp
                i +=1
            return p2
        
        return max(helper(1, len(nums)-1), helper(0,len(nums)-2))
