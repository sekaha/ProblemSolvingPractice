class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        queue = []
        max_size = 1
        sizes = {c: 1 for c in set(s)}
        budgets = {c: k for c in set(s)}

        for i, c in enumerate(s[1:]):
            if c == s[i - 1]:
                print("added")
                sizes[c] += 1
            elif c in queue and budgets[c]:
                print("added")
                budgets[c] -= 1
                sizes[c] += 1
            else:
                budgets[c] = k
                sizes[c] = 1

            max_size = max(sizes[c], max_size)
            queue.append(c)

            if i > k:
                queue.pop(0)

        return max_size + 1


sol = Solution()
print(sol.characterReplacement("AABABBAAAAAAAABA", 2))
