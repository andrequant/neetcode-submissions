class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        c = 0
        prod = 1
        l = 0

        for r in range(n):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod //= nums[l]
                l += 1

            c += (r - l + 1)
        
        return c



