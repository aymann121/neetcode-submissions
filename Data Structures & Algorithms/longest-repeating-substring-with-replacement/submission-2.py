class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 1
        total = 1
        freq = {s[0]: 1}
        p1, p2 = 0,0
        res = 1

        while p2 < len(s) -1:
            while total - maxf <= k and p2 <len(s)-1:
                p2 +=1
                freq[s[p2]] = freq[s[p2]] + 1 if s[p2] in freq else 1
                if freq[s[p2]] > maxf:
                    maxf = freq[s[p2]]
                total += 1
                if total - maxf <= k:
                    res = max(res, total)
                print(p1, p2)
            while total - maxf > k:
                
                freq[s[p1]] -= 1
                p1 += 1
                total -= 1
        return res
            



        