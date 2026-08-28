class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = []
        cycle.append(n)
        if n == 1:
            return True
        while n != 1:
            b = list(str(n))
            c = [int(i)**2 for i in b]
            n = sum(c)
            if n in cycle:
                return False
            elif n == 1:
                return True
            else:
                cycle.append(n)