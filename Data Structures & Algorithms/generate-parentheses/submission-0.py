class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        #conditions 
        def backtrack(opened, closed):
            if opened == n and closed == n:
                res.append("".join(cur))
                return 
            if opened == n and closed != n:
                cur.append(')')
                backtrack(opened, closed+1)
                cur.pop()
            elif opened == closed:
                cur.append('(')
                backtrack(opened +1, closed)
                cur.pop()
            elif opened > closed:
                cur.append('(')
                backtrack(opened +1, closed)
                cur.pop()
                cur.append(')')
                backtrack(opened , closed+1)
                cur.pop()
        backtrack(0,0)
        return res

