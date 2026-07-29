class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndexMap = {}
        for i, e in enumerate(nums):
            if target - e in numIndexMap:
                return [numIndexMap[target - e], i] 
            numIndexMap[e] = i
            
