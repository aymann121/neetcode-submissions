class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        maxRight = [0] * len(height)
        res = 0 

        maxSoFar = 0 
        for i in range(len(height)):
            maxLeft[i] = maxSoFar
            maxSoFar = max(maxSoFar, height[i])

        maxSoFar = 0 
        for i in range(len(height)-1, -1, -1):
            maxRight[i] = maxSoFar
            maxSoFar = max(maxSoFar, height[i])

        for i in range(len(height)):
            res += max(min(maxLeft[i],maxRight[i])-height[i], 0)

        return res
        