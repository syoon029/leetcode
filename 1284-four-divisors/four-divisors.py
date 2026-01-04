class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        
        def find_divisors(num):
            sets=set()
            for i in range(1, int(num ** 0.5)+1):
                if num % i == 0:
                    sets.add(i)
                    sets.add(num // i)
            
            if len(sets) == 4:
                return sets
                
            else:
                return None
        
        for n in nums:
            div = find_divisors(n)
            if div:
                result += sum(div)
        
        return result
            

