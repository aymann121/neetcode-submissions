class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1 = 0 
        ptr2 = len(heights)-1
        maxArea = min(heights[ptr1], heights[ptr2]) * (ptr2-ptr1)

        while ptr1 < ptr2:
            if heights[ptr1] < heights[ptr2]:
                ptr1 +=1
            elif heights[ptr1] > heights[ptr2]:
                ptr2 -=1
            else:
                if heights[ptr1+1] < heights[ptr2-1]:
                    ptr2 -=1
                else:
                    ptr1 +=1
            maxArea = max(maxArea, min(heights[ptr1], heights[ptr2]) * (ptr2-ptr1))
            print(ptr1,ptr2)
        return maxArea
