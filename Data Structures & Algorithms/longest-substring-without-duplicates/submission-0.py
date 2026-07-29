class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        found = {}
        start = 0

        for i, c in enumerate(s):
            if c in found:
                while s[start] != c:
                    del found[s[start]]
                    start += 1
                found[s[start]] = i
                start += 1
            else:
                found[s[i]] = c
            maxLength = max(maxLength, i-start+1)
        return maxLength