class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_element = 0
        max_count = 0
        l = 0

        # max f doesn't need to be proper, so we can just keep max_f constant even if it's not true for our current window window
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_element = max(max_element, counts[s[r]])

            # invalid window, shift until valid
            while (r - l + 1) - max_element > k:
                counts[s[l]] -= 1
                l += 1

            max_count = max(max_count, r - l + 1)

        return max_count


sol = Solution()
print(sol.characterReplacement("AABABBA", 1))
