class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {c: 0 for c in set(s)}
        counts[s[0]] = 1
        max_length = 0
        l = 0

        # maybe use a max heap
        for r in range(len(s)):
            # check if the amount of max occuring chars in the string
            # make up len-k elements of that string, otherwise, start moving left pointer
            focus = max(list(counts.keys()), key=lambda x: counts[x])[0]
            while counts[focus] <= r - l - k:  # traversed thus far -k
                l += 1
                counts[s[1]] -= 1
                focus = max(list(counts.keys()), key=lambda x: counts[x])[0]
            max_length = max(r - l, max_length)
            counts[s[r]] += 1

        return max_length


sol = Solution()
print(sol.characterReplacement("ABAB", 2))
