import re

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        final = ""

        # formatting
        for s in strs:
            s = s.replace("\\","\\\\")
            s = s.replace(":","\\:")

            final += s+":"

        return final

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, s):
        output = []
        tmp = ""
        i = 0

        while i < len(s):
            if s[i] == "\\": # skip for escape character
                tmp += s[i+1]
                i+=2
            
            if s[i] == ":":
                output.append(tmp)
                tmp = ""
            else:
                tmp += s[i]
            
            i += 1

        return output

sol = Solution()
test1 = sol.encode(["hello","\\","world"])
test2 = sol.encode(["hello",":","world"])
print(test1, test2)
print(sol.decode((test1)))
print(sol.decode((test2)))