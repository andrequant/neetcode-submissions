class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = target - nums[i]
            new_nums = nums[:i] + nums[i+1:]
            if  a in new_nums:
                return [i, new_nums.index(a)+1]