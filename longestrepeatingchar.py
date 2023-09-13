class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {c: 0 for c in set(s)}
        most_frequent = None
        dist = 0
        l, r = 0, 0

        while l != len(s) and r != len(s):
            most_frequent = max(counts.values())

            # valid window
            if (r - l) - most_frequent <= k:
                counts[s[r]] += 1
                r += 1
            else:  # invalid window, shift until valid
                counts[s[l]] -= 1
                l += 1

        return dist


sol = Solution()
print(sol.characterReplacement("AAAA", 2))
