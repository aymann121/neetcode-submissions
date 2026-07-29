class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()

        def backtracking(i, total):
            if total == target: 
                res.append(cur.copy())
                return
            if total >= target: return 
            if i >= len(candidates): return

            cur.append(candidates[i])
            backtracking(i+1, total+candidates[i])
            cur.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i +=1

            backtracking(i+1, total)

        backtracking(0,0)
        return res
