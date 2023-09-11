class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def recursive(a=1, b=1):
            if a == m and b == n:
                return 1  # base case, path found

            l, r = 0, 0

            if a != m:
                l = recursive(a + 1, b)

            if b != n:
                r = recursive(a, b + 1)

            return r + l

        return recursive()


sol = Solution()

for x in range(1, 10):
    for y in range(1, 10):
        print(x, y, sol.uniquePaths(x, y))
