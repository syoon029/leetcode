class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = ''.join(txt for txt in s if txt.isalnum())
        clean = lower(clean)
        return clean == clean[::-1]