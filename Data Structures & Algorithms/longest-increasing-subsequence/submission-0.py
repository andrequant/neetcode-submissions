class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n =  len(nums)
        subs = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    subs[i] = max(subs[i], subs[j] + 1)

        return max(subs)