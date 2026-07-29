class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r = 1, max(piles)
        res = r

        def hoursTaken(k):
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(float(piles[i])/k)
            return hours

        while l<=r:
            m = (r+l) //2
            hours = hoursTaken(m)
            if hours > h:
                l = m+1
            else:
                r = m-1
                res = m
                
        return res
