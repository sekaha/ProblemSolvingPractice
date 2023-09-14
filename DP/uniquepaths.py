class Solution:
    def uniquePaths(self, w: int, h: int) -> int:
        w, h, result = w - 1, h - 1, 1

        for i in range(w):
            result *= (h + w) - i
            result //= i + 1

        return result


sol = Solution()
print(sol.uniquePaths(10, 10))
