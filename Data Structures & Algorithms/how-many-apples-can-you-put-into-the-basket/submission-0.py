class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        c = 0
        total = 0
        weight.sort()
        for apple in weight:
            total += apple
            if total > 5000:
                break
            else:
                c += 1
        
        return c