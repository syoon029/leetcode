class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5)+1):
                if n % i == 0:
                    return False
            return True

        for num in nums:
            n = round(num ** (1.0/3))
            if is_prime(n) and n ** 3 == num:
                result += 1 + n + n*n + num
                continue
            
            for i in range(2, int(num ** 0.5)+1):
                if num % i == 0:
                    j = num // i
                    if i != j and is_prime(i) and is_prime(j):
                        result += 1 + i + j + num
                        
                    
        
        return int(result)
            

