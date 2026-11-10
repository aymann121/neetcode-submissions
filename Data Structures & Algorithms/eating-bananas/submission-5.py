class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(val):
            takes = 0
            for e in piles:
                takes += math.ceil(e/val)
            return takes <= h
        
        def binarySearch(l, r):
            valid = -1
            while l<= r:
                m = (l + r) // 2
                if check(m):
                    valid = m
                    r = m-1
                else:
                    l = m +1
            return valid

        return binarySearch(1, max(piles))