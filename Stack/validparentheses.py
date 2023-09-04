class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {"(":")","{":"}","[":"]"}
        stack = []

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not (len(stack) > 0 and (pairs[stack.pop()]==c)):
                    return False
        
        return len(stack)==0


sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("()[]{)}"))