class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            # checking for even and odd strings
            for r_off in range(2):
                r, l = i + r_off, i

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1

                longest = max(longest, s[l + 1 : r], key=len)

        return longest


sol = Solution()
print(sol.longestPalindrome("bb"))
print(sol.longestPalindrome("bbabc"))
print(sol.longestPalindrome("xaabacxcabaax"))
