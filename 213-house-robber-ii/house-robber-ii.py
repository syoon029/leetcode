class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return nums[0]

        rob_money = [0] * n #  0 - n-1
        rob_money[0] = nums[0]
        rob_money[1] = max(nums[0], nums[1])

        rob_money2 = [0] * n # 1 - n
        rob_money2[0] = 0
        rob_money2[1] = nums[1]
        

        if n >= 3:
            for i in range(2,n-1):
                rob_money[i] = max(rob_money[i-2] + nums[i] , rob_money[i-1])
            for j in range(2, n):
                rob_money2[j]  = max(rob_money2[j-2] + nums[j] , rob_money2[j-1])
            
            rob_money[n-1] = rob_money[n-2]
        
        return max(rob_money[n-1], rob_money2[n-1])

            
       
            
        return rob_money[n-1]
       
