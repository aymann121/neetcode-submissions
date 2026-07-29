class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMult = [1] * len(nums)
        rightMult = [1] * len(nums)
        output = [1] * len(nums)

        leftMult[0] = nums[0]
        for i in range(1,len(nums)):
            leftMult[i] = leftMult[i-1] * nums[i]
        
        rightMult[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            rightMult[i] = rightMult[i+1] * nums[i]
        
        output[0] = rightMult[1]
        output[-1] = leftMult[-2]
        for i in range(1, len(nums)-1):
            output[i] = rightMult[i+1] * leftMult[i-1]
        return output