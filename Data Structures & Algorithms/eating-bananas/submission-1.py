class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l <= r:
            m = (l+r)//2

            ho = self.hours(piles, m)

            if ho > h:
                l = m + 1
            elif ho <= h:
                r = m - 1

        return l



    def hours(self, piles, k):
        hours = 0
        for bananas in piles:
            hours += bananas // k + (1 if bananas % k > 0 else 0)

        return hours
