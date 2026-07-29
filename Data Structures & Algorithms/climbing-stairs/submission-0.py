class Solution:
    def climbStairs(self, n: int) -> int:
        p1, p2 = 1, 0

        for i in range(n):
            temp = p1
            p1 = p1 + p2
            p2 = temp
        return p1
        