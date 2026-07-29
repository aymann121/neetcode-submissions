class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur = []
        res = []
        def backtracking(arr, target):
            if target == 0:
                res.append(cur.copy())
                return
            elif target < 0 or arr == []:
                return 
            
            cur.append(arr[0])
            backtracking(arr, target-arr[0])
            cur.pop()

            backtracking(arr[1:], target)
        backtracking(nums, target)
        return res
