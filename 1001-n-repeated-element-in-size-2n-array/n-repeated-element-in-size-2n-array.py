from collections import Counter
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        cnt = Counter(nums)
  
        for k, i in cnt.items():
            if i == n:
                return k
        