class Solution:
    def uniquePaths(self, w: int, h: int) -> int:
        result = 1

        for i in range(w - 1):
            result *= (h + w - 2) - i
            result //= i + 1

        return result


sol = Solution()
print(sol.uniquePaths(10, 10))
