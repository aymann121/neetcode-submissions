class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}

        def helper(s):
            if s in memo:
                return memo[s]
            if len(s) == 0: return 1
            if len(s) == 1: return 1 if s != '0' else 0
            
            res = 0
            if s[0] != '0': res += helper(s[1:]) 
            if int(s[0:2]) < 27 and s[0] != '0':  res += helper(s[2:])
            memo[s] = res
            return res

        return helper(s)
