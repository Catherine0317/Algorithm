class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if len(points) < 1:
            return 0
        else:
            points.sort(key = lambda x:x[1])
            temp = points[0][1]
            count = 1
            for i in range(1,len(points)):
                if temp >= points[i][0]:
                    continue 
                else:
                    temp = points[i][1]
                    count += 1

            return count 
