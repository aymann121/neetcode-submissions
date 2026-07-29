class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()

        for r in range(len(s2)):
            window[s2[r]] += 1

            if r >= len(s1):
                left = s2[r - len(s1)]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]

            if window == need:
                return True

        return False
            

