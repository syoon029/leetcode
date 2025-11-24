class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # left = 0
        # right = len(numbers) -1

        # while left < right:
        #     s= numbers[left] + numbers[right]
        #     if s == target:
        #         return [left+1, right+1]
            
        #     elif s < target:
        #         left += 1
        #     else:
        #         right -= 1
        dicts={}

        for i, num in enumerate(numbers):
            if target - num in dicts:
                return [ dicts[target-num]+1, i+1]
            dicts[num] = i
     

                

                
        
        