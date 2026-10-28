class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        pass

        dp = [0] * (high+1)
        dp[0] = 1

        # let's calculate for all sizes:
        # for size n, the number of ways (number(n)) is number(n-one) + number(n-zero)
    

        for n in range(1, high+1):

            dp[n] = (dp[n - zero] if n - zero >= 0 else 0) + (dp[n - one] if n - one >= 0 else 0)

        return sum(dp[low:high+1]) % 1000000007