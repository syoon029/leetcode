from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(int)
        
        for i in nums:
            count[i] += 1
        
        return sorted(count, key=count.get, reverse=True)[:k]
    
        
