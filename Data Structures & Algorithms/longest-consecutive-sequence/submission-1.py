class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        elementSet = set(nums)
        record = {}
        for e in elementSet:
            temp = e
            val = 1
            while temp+1 in elementSet:
                if temp+1 in record:
                    val += record[temp+1]
                    break
                else:
                    val += 1
                    temp += 1
            record[e] = val
        return max(record.values())
                