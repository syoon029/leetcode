class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            candidate = -1
            num = 1
            while (nums[i] & num) != 0:
                candidate = nums[i]-num
                num <<=1
            nums[i] = candidate
        return nums