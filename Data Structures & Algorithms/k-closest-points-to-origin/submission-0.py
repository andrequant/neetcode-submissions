class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.points = points
        self.k = k
        self.quickSort(self.points, 0, len(points)-1)
        return self.points[:self.k]

    def quickSort(self, points, s, e):
        if e-s <= 0:
            return points

        pivot = self.points[e]
        left = s

        for i in range(s,e):
            if self.distance(self.points[i]) <= self.distance(pivot):
                tmp = self.points[left]
                self.points[left] = self.points[i]
                self.points[i] = tmp
                left += 1
        
        self.points[e] = self.points[left]
        self.points[left] = pivot

        self.quickSort(self.points, s, left-1)
        self.quickSort(self.points, left, e)


    def distance(self,point):
        return (point[0]**2 + point[1]**2)**0.5