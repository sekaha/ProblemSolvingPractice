class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {c: 0 for c in set(s)}
        most_frequent = None
        dist = 0
        l, r = 0, 0

        while l != len(s) and r != len(s):
            most_frequent = max(counts.values())

            while r - l - k < most_frequent:
                counts[s[r]] += 1
                r += 1
                dist = max(r - l, dist)
            else:
                counts[s[l]] -= 1
                l += 1

        return dist


sol = Solution()
print(sol.characterReplacement("AABABBA", 1))
