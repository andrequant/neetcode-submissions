class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        i = 0
        
        merged = [intervals[0]]

        while i < len(intervals)-1:
            m = self.mergeTwo(merged[-1], intervals[i+1])
            if m:
                merged[-1] = m
            else:
                merged.append(intervals[i+1])
            i += 1

        return merged



    def mergeTwo(self, inter1, inter2):
        
        inter_new = [0,0]

        if (inter1[0] <= inter2[0] <= inter1[1]):
            inter_new[0] = inter1[0]
            inter_new[1] = max(inter1[1], inter2[1])
            return inter_new
        else:
            return None