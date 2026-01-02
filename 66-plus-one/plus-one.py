from collections import deque

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits = deque(digits)

        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return list(digits)
            else:
                while digits[i] == 9:
                    digits[i] = 0
                    i -= 1
                if i >= 0:
                    digits[i] += 1
                else:
                    digits.appendleft(1)
                return list(digits)
                    



