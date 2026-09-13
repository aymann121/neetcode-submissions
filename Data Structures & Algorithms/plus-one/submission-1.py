class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = digits
        isNine = True
        for i in range(len(res)-1, -1, -1):
            if res[i] != 9:
                res[i] += 1
                isNine = False
                break
            else:
                res[i] = 0

        if isNine:
            res = [1] + res
        return res
         
