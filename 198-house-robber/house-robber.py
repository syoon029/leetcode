class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n < 2:
            return nums[0]

        max_money = [0] * n
        max_money[0] = nums[0]
        max_money[1] = max(nums[1], max_money[0])

        for i in range(2, n):
            max_money[i] = max(max_money[i-2] + nums[i], max_money[i-1])
            print(max_money)
        
        return max_money[n-1]