class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        req_time = 0
        for i in range(len(points)-1):
            x,y = points[i]
            x2,y2 = points[i+1]
            min_time = max(abs(x2-x), abs(y2-y))
            req_time += min_time
        
        return req_time