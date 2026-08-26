class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.l = []
        self.ma = 0
        

    def next(self, val: int) -> float:
        self.l.append(val)
        if len(self.l) > self.size:
            self.l.pop(0)
        self.ma = sum(self.l)/len(self.l)
        return self.ma


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
