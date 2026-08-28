class Solution:
    def countElements(self, arr: List[int]) -> int:
        c = 0
        s_arr = set(arr)
        for i in arr:
            if i + 1 in s_arr:
                c += 1
        return c
        