class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def d_cal(point1,point2):
            x1,y1=point1
            x2,y2=point2
            return max(abs(x1-x2),abs(y1-y2))
        res=0
        for i in range(1,len(points)):
            res+=d_cal(points[i],points[i-1])
        return res
