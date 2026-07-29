class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #create maxleft and maxright arrays on nums partitioned with size k

        maxLeft = nums.copy()
        maxRight = nums.copy()

        maxL, maxR = nums[0], nums[-1]

        for i in range(len(nums)):
            
            if i % k == 0:
                maxL = nums[i]
            maxL = max(maxL, nums[i])
            maxLeft[i] = maxL
        
        for i in range(len(nums)-1, -1, -1):
            if i % k == k-1:
                maxR = nums[i]
            maxR = max(maxR, nums[i])
            maxRight[i] = maxR
        
        res = []
        for i in range(0, len(nums)-k+1):
            res.append(max(maxLeft[i+k-1], maxRight[i]))
        return res
        