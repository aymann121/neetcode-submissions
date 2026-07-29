class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedArr = sorted(nums)
        i = 0
        res = []
        
        def nextNumber(ptr):
            number = sortedArr[ptr]
            while ptr < len(sortedArr):
                ptr += 1
                if ptr<len(sortedArr) and number != sortedArr[ptr]:
                    break
            return ptr

        while i < len(sortedArr)-1:
            ptr1 = i+1
            ptr2 = len(sortedArr)-1
            while ptr1 < ptr2:
                if sortedArr[i] + sortedArr[ptr1] + sortedArr[ptr2] == 0:
                    res.append([sortedArr[i], sortedArr[ptr1], sortedArr[ptr2]])
                    ptr1 = nextNumber(ptr1)
                elif sortedArr[i] + sortedArr[ptr1] + sortedArr[ptr2] < 0:
                    ptr1 += 1
                else:
                    ptr2 -= 1
            i = nextNumber(i)
        return res
                
