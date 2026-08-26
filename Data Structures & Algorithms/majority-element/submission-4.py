class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        size_m = len(nums)//2
        for i,n in enumerate(nums):
            if n not in d.keys():
                d[n] = 0
            d[n] += 1
            if i+1 > size_m:
                if d[n] > size_m:
                    return n