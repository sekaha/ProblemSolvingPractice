class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        runs = 0
        memo = {}

        def recursive(a=1, b=1):
            nonlocal runs
            runs += 1

            if (a, b) in memo:
                return memo[a, b]

            if a == m and b == n:
                return 1  # base case, path found

            l, r = 0, 0

            if a != m:
                l = recursive(a + 1, b)

            if b != n:
                r = recursive(a, b + 1)

            memo[(a, b)] = r + l

            return memo[(a, b)]

        ans = recursive()
        print(runs)
        return ans


sol = Solution()

print(sol.uniquePaths(3, 7))
