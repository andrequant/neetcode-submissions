class Solution:
    def __init__(self):
        self.cases = {}
    def climbStairs(self, n: int) -> int:
        s = 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 0:
            return 0
        else:
            if n-1 in self.cases.keys():
                _n1 = self.cases[n-1]
            else:
                _n1 = self.climbStairs(n-1)
                self.cases[n-1] = _n1
            if n-2 in self.cases.keys():
                _n2 = self.cases[n-2]
            else:
                _n2 = self.climbStairs(n-2)
                self.cases[n-2] = _n2
            s += _n1 + _n2
        
        return s
        
