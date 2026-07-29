class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        elementSet = set(nums)
        record = {}
        visited = set()
        for e in elementSet:
            if e in visited:
                continue
            temp = e
            val = 1
            while temp+1 in elementSet:
                if temp+1 in record:
                    val += record[temp+1]
                    break
                else:
                    visited.add(temp+1)
                    val += 1
                    temp += 1
            record[e] = val
            visited.add(e)
        return max(record.values())
                