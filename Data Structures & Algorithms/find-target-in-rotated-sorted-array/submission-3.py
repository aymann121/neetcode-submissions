class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot():
            if nums[-1] > nums[0] or len(nums) == 1: 0
            res = 0
            l, r = 1, len(nums)-1
            while l <= r:
                m = r+l //2 
                if nums[m] < nums[0]:
                    r = m-1
                    res = m
                else:
                    l = m+1
                    res = m+1
            return res
        
        def binarySearch(l,r):
            while l <= r:
                m = (l+r) //2
                if target < nums[m]:
                    r = m-1
                elif target > nums[m]:
                    l = m+1
                else:
                    return m
            return -1
        
        p = findPivot()
        v1 = binarySearch(0, p-1)
        if v1 != -1:
            return v1
        v2 = binarySearch(p, len(nums)-1)
        if v2 != -1:
            return v2
        return -1
            
        