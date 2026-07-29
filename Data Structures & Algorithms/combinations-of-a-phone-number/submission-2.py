class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        mapping = {2: ['a','b','c'],
         3: ['d','e','f'], 
         4: ['g','h','i'],
         5: ['j','k','l'], 
         6: ['m','n','o'],
         7: ['p','q','r','s'], 
         8: ['t','u','v'],
         9: ['w','x','y','z'],}

        res = []
        cur = []
        def backtracking(nums):
            if nums == "":
                res.append("".join(cur))
                return 
            num = int(nums[0])
            for c in mapping[num]:
                cur.append(c)
                backtracking(nums[1:])
                cur.pop()
        backtracking(digits)
        return res