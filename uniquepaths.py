from functools import reduce


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def choose(n, k):
            fact = (
                lambda x: reduce(lambda a, b: a * b, range(1, x + 1)) if (x > 0) else 1
            )
            return int(fact(n) / (fact(k) * fact(n - k)))

        return choose(n + (m - 2), m - 1)


sol = Solution()

# for x in range(1, 5):
#    for y in range(1, 10):
print(sol.uniquePaths(3, 7))
