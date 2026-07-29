class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, e in enumerate(temperatures):
            while stack and stack[-1][1] < e:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i,e))
        return res
