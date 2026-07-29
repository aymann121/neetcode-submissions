class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = {}
        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in freqMap:
                freqMap[sortedStr].append(s)
            else:
                freqMap[sortedStr] = [s]
        res = [v for v in freqMap.values()]
        return res

        