class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r = 1, max(piles)


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
                
        if m != 1 and hoursTaken(m-1) <= h:
            return m-1
        if hoursTaken(m) <= h:
            return m
        return m+1
