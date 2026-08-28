class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.nums = nums[:k]
        

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
        elif val > min(self.nums):
            self.nums.remove(min(self.nums))
            self.nums.append(val)

        print(self.nums)
        return min(self.nums)

