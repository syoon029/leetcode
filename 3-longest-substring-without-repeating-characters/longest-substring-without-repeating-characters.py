import itertools
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        result = 0

        visited = set()
        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left +=1
            visited.add(s[right])
            result = max(result, right - left +1)
        
        return result
