class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []
        def backtracking(arr):
            if arr == []:
                res.append(cur.copy())
                return

            cur.append(arr[0])
            backtracking(arr[1:])
            cur.pop()

            backtracking(arr[1:])
        backtracking(nums)
        return res