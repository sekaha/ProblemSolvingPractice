class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_string = 0
        window = {c: 0 for c in set(s)}

        for c in s:
            pass


sol = Solution()
print(sol.characterReplacement("ABAB", 2))
