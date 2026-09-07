class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1:
            return intervals

        intervals.sort()

        i = 0
        
        merged = [intervals[0]]

        while i < len(intervals)-1:
            if (intervals[i+1][0] <= merged[-1][1]):
                merged[-1][1] = max(merged[-1][1], intervals[i+1][1])
            else:
                merged.append(intervals[i+1])
            i += 1

        return merged