class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s))+'#'+s for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        ptr = 0
        i = 0
        while i < len(s):
            if s[i] == "#":
                length = int(s[ptr:i])
                res.append(s[i+1:i+1+length])
                i += length + 1
                ptr = i
            else:
                i += 1
        return res

            
            
