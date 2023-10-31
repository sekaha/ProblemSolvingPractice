from LED import *


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        runs = 0
        memo = {}

        def recursive(x=1, y=1):
            nonlocal runs
            runs += 1

            if (x, y) in memo:
                return memo[x, y]

            if x == m and y == n:
                return 1  # base case, path found

            l, r = 0, 0

            if x != m:
                l = recursive(x + 1, y)

            if y != n:
                r = recursive(x, y + 1)

            memo[(x, y)] = r + l

            return memo[(x, y)]

        ans = recursive()
        print(runs)
        return ans


sol = Solution()

for x in range(3, 10):
    y = 2
    print(x, y, sol.uniquePaths(x, y))
