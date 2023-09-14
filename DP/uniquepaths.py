class Solution:
    def uniquePaths(self, w: int, h: int) -> int:
        result = 1

        for i in range(1, w):
            result = result * (h + i - 1) // i

        return result


sol = Solution()
print(sol.uniquePaths(10, 10))
