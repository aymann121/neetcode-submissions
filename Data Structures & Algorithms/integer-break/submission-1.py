class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        if n == 4: return 4
        exp = ((n-2)//3)
        remaining = n - (3*exp)
        print(exp, remaining)
        return 3**exp * remaining
        