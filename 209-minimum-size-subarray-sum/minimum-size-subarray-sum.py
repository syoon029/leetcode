class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        summ = 0
        min_leng = float('inf')

        for end in range(len(nums)):
            summ += nums[end]

            while summ >= target:
                min_leng = min(min_leng, end-start+1)
                summ -= nums[start]
                start+=1
        
        if min_leng == float('inf'):
            return 0
        else:
            return min_leng 
       