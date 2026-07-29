class Solution:

    def encode(self, strs: List[str]) -> str:
        singleStr = ""
        for e in strs:
            singleStr += str(len(e)) + "#" + e
        return singleStr

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while(i < len(s)):
            number = s[i]
            while s[i+1] != "#":
                number += s[i+1]
                i += 1
            i += 1
            out.append(s[i+1: i + int(number)+1])
            i += int(number)+1
        return out 