class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            orgin = num
            candidate = -1
            for j in range(1, orgin):
                if (j | (j+1)) == orgin:
                    candidate = j
                    break
            ans.append(candidate)
        
        return ans