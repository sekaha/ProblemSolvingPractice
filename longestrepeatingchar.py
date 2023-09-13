class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {c: 0 for c in set(s)}
        l, r = 0, 0
        max_element = 0
        max_length = 0

        # max f doesn't need to be proper, so we can just keep max_f constant even if it's not true for our window
        while r < len(s):
            counts[s[r]] += 1
            max_element = max(max_element, counts[s[r]])
            r += 1

            # invalid window, shift until valid
            while (r - l) - max_element > k:
                counts[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l)

        return max_length


sol = Solution()
print(sol.characterReplacement("AABABBA", 1))
