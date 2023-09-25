class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1

        for _ in range(abs(n)):
            res *= x

        return res if n > 0 else 1 / res


sol = Solution()
print(sol.myPow(2.1, 3))
