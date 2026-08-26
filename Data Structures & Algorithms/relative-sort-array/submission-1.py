class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        c = {}

        for element in arr2:
            d[element] = arr1.count(element)

        left = list(set(arr1) - set(arr2))
        left.sort()

        for element in left:
            c[element] = arr1.count(element)

        d.update(c)
        print(d)
        l = []
        for k,e in d.items():
            ll = [k] * e
            l.extend(ll)

        return l
