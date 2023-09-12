class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {c: 0 for c in set(s)}
        traversed = 0
        l = 0
        max_length = 0

        for r in range(len(s)):
            # local max string length found, moving left pointer until the starting char makes up r-k characters
            while counts[s[l]] <= traversed - k:
                counts[s[l]] -= 1
                l += 1
                traversed -= 1
            max_length = max(traversed, max_length)
            traversed += 1
            counts[s[r]] += 1

            print(s[l : r + 1])
        return max_length


sol = Solution()
print(sol.characterReplacement("ABABCCC", 2))
