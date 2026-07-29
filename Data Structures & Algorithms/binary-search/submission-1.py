class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, m, r = 0, (len(nums)-1)//2, len(nums)-1

        while l <= r:
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m-1
            else:
                l = m+1
            m = (r+l) //2
        return -1
        