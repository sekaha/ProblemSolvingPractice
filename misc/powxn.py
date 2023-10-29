from math import floor, ceil


class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}

        def helper(x, n):
            if (x, n) in memo:
                return memo[(x, n)]

            if n == 0:
                v = 1
            elif n == 1:
                v = x
            elif n == 2:
                v = x * x
            else:
                v = helper(x, floor(n / 2)) * helper(x, ceil(n / 2))
            memo[(x, n)] = v

            return memo[(x, n)]

        return 1 / helper(x, abs(n)) if n < 0 else helper(x, abs(n))


sol = Solution()
print(sol.myPow(2.1, 3))
print(sol.myPow(2, 10))
print(sol.myPow(2, -1))
print(sol.myPow(2, 0))
print(sol.myPow(0.00001, 2147483647))
