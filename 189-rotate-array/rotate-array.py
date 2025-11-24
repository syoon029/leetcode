class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        answer =[0] * len(nums)
        for i in range(len(nums)):
            answer[(i+k) % len(nums)] = nums[i]
        
        for i in range(len(nums)):
            nums[i] = answer[i]
        
        

        
        
            
        