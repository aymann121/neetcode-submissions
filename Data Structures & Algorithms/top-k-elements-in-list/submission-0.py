from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = Counter(nums)
        bucketlist = [[] for i in range(len(nums))] 

        for key, v in freqmap.items():
            bucketlist[v-1].append(key)
        res = []
        k_remaining = k
        for i in range(len(bucketlist)-1, -1, -1):
            if k_remaining == 0:
                return res
            res.extend(bucketlist[i][:k_remaining])
            k_remaining -= min(k_remaining, len(bucketlist[i]))
        return res
            
