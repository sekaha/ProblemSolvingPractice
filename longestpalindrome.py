class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            # checking for even and odd strings
            for l_off in range(2):
                l, r = i + l_off, i
                pal = ""

                while r >= 0 and l < len(s) and s[l] == s[r]:
                    if r != l:
                        pal = s[l] + pal + s[r]
                    else:
                        pal = s[l]
                    r -= 1
                    l += 1

                if len(longest) < len(pal):
                    longest = pal
                    print(longest)

        return longest


sol = Solution()
print(sol.longestPalindrome("bb"))
print(sol.longestPalindrome("babbc"))
print(sol.longestPalindrome("xaabacxcabaax"))
