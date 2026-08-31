class Solution:
    def __init__(self):
        self.scorecard = []

    def calPoints(self, operations: List[str]) -> int:
        for operation in operations:
            try:
                operation = int(operation)
                self.new_score(operation)
            except:
                if operation == '+':
                    self.plus()
                elif operation == 'D':
                    self.double()
                elif operation == 'C':
                    self.invalidate()

        return sum(self.scorecard)


    def new_score(self, value):
        self.scorecard.append(int(value))

    def plus(self):
        _1 = self.scorecard[-1]
        _2 = self.scorecard[-2]
        self.scorecard.append( _1 + _2)

    def double(self):
        self.scorecard.append(2*self.scorecard[-1])
    
    def invalidate(self):
        self.scorecard.pop()

