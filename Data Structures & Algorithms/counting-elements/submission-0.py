class Solution:
    def countElements(self, arr: List[int]) -> int:
        c = 0
        for i in arr:
            if i + 1 in arr:
                c += 1
        return c
        