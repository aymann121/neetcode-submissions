from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for e in freq:
            if freq[e] > len(nums) // 2:
                return e
        return -1