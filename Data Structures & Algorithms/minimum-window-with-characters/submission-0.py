class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def geq(d1, d2):
            res = True
            for e in d1:
                if e not in d2 or d2[e] < d1[e]:
                    res = False
            return res

        freq1 = Counter(t)
        freq2 = Counter()
        res = ""

        p1, p2 = 0, 0
        while p2 < len(s):
            freq2[s[p2]] += 1

            if geq(freq1, freq2):
                while geq(freq1, freq2):
                    if res == "" or len(res) > p2+1-p1:
                       res = s[p1:p2+1]
                    freq2[s[p1]] -= 1
                    p1 += 1
                p1 -=1
                freq2[s[p1]] += 1
            p2 += 1
        return res 

            