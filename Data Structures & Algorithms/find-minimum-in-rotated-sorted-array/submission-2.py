class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0] or len(nums) == 1: return nums[0]
        
        res = 0
        l, r = 1, len(nums)-1
        while l <= r:
            m = r+l //2 
            if nums[m] < nums[0]:
                r = m-1
                res = nums[m]
            else:
                l = m+1
                res = nums[m+1]
        return res
        


        