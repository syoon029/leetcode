class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        new_interval = []
        intervals.sort(key=lambda x:x[0])

        for i in intervals:
            if not new_interval or new_interval[-1][1] <i[0]:
                new_interval.append(i)
            else:
                new_interval[-1][1] = max(new_interval[-1][1], i[1])

        return new_interval
            
        