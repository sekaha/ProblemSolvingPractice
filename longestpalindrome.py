class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            l = i
            r = len(s) - 1

            s_l, s_r = "", ""

            while r >= l:
                if s[l] == s[r]:
                    if l != r:
                        s_l = s_l + s[l]
                    s_r = s[r] + s_r
                    l += 1
                    r -= 1
                else:
                    s_l, s_r = "", ""

                    if s[l] != s[r]:
                        r -= 1

            r = len(s) - 1

            longest = s_l + s_r if len(longest) < len(s_l + s_r) else longest

        return longest


sol = Solution()
print(sol.longestPalindrome("xaabacxcabaax"))
