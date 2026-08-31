class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        i = 0
        while i < len(nums):
            j = 0
            while i+j < len(nums) and nums[i+j] == 1:
                j += 1

            if j > m:
                m = j
                i += j
            else:
                i += 1

        return m


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res,count = 0,0
        for num in nums:
            count = count+1 if num else 0
            res = max(count,res)
        return res