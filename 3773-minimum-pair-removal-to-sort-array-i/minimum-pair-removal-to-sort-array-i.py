class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        count =0 
        while len(nums) > 1:
            isAsc = True
            minSum = float("inf")
            idx =-1
            
            for i in range(len(nums)-1):
                pair = nums[i] + nums[i+1]

                if nums[i] > nums[i+1]:
                    isAsc = False
                
                if pair < minSum:
                    minSum = pair
                    idx = i
                
            if isAsc:
                break

            count +=1
            nums[idx] = minSum
            nums.pop(idx + 1)

        return count        
