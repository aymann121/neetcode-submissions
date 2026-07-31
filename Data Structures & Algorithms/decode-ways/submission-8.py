class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}

        def helper(s):
            if s in memo:
                return memo[s]
            if len(s) == 0: return 1
            if len(s) == 1: return 1 if s != '0' else 0
            
            res = -1
            val = int(s[0:2])
            if (val > 26 and s[1] == '0') or val < 10:
                res = 0
            else: #take 1
                if val == 10 or val == 20:
                    res = helper(s[2:])
                elif (val > 26): res = helper(s[1:])
                else: res = helper(s[1:]) + helper(s[2:])
            memo[s] = res
            return res

        return helper(s)