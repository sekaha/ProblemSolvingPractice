class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        focus = 0
        budget = k
        max_size = 0

        for i in range(len(s)):
            if budget > 0:
                if s[focus] != s[i]:
                    budget -= 1
            else:
                while s[focus + 1] == s[focus + 1]:
                    focus += 1
                budget = k
            max_dist = max(max_size, i - focus)


sol = Solution()
print(sol.characterReplacement("ABAB", 2))
