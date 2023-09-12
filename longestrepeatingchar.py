class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        queue = []
        max_size = 0
        sizes = {}

        for i, c in enumerate(s):
            if c in queue:
                sizes[c] += 1
            else:
                sizes[c] == 0s
            queue.append(c)

            if i > k:
                queue.pop(0)


sol = Solution()
sol.characterReplacement("ABAB", 2)
