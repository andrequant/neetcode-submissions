class Solution:
    def mySqrt(self, x: int) -> int:

        c1 = 0
        c2 = x


        for i in range(x+1):
            mid = (c1 + c2)//2
            if c1 * c1 <= x < (c1+1)*(c1+1):
                return c1
            elif (c1+1)*(c1+1) == x:
                return c1 + 1
            elif c2 * c2 == x:
                return c2
            elif c1 * c1 < x < mid * mid:
                c2 = mid
            elif mid * mid <= x < c2 * c2:
                c1 = mid
            