class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # remove none alphanumeric characters
        cleaned = [c for c in s.lower() if c.isalnum()]

        for i in range(len(cleaned)//2):
            if cleaned[i] != cleaned[len(cleaned)-i-1]:
                return False

        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))