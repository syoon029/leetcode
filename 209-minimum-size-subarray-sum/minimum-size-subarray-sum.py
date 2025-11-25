class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        total =0
        start =0
        min_len = float('inf')

        for end in range(len(nums)):
            total += nums[end]

            while total >= target:
                min_len = min(min_len, end-start +1)
                total -= nums[start]
                start +=1
        
        if min_len == float('inf'):
            return 0
        else:
            return min_len
            
        