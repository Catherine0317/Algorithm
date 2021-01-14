class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) <= 1:
            return 0
        else:
            intervals.sort(key = lambda x:x[1])
            res = [intervals[0]]
            for i in range(1,len(intervals)):
                if intervals[i][0] >= res[-1][1]:
                    res.append(intervals[i])
            return len(intervals)-len(res)
        
