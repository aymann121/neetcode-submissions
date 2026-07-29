class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        val = (0,0,0)
        for i, e in enumerate(heights):
            if stack and stack[-1][0] > e:
                while stack and stack[-1][0] > e:
                    val = (e, i, stack[-1][2] + i- stack[-1][1])
                    maxArea = max(maxArea, (val[2])* stack[-1][0])
                    stack.pop()
                stack.append(val)
            elif not (stack and stack[-1][0] == e):
                stack.append((e,i,0))

        while stack:
            v = stack.pop()
            maxArea = max(maxArea, (v[2]+ len(heights)-v[1]) * v[0])
        return maxArea
