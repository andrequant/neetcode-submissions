class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while j <= len(nums)-1 and i <= len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
            j += 1