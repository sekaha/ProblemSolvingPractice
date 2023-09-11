class Solution:
    def uniquePaths(self, w: int, h: int) -> int:
        # finding the natural, triangular, tetrahedral etc numbers depending on inputs
        n, k = h + (w - 2), w - 1
        fact = 1

        # binomial coefficinet
        for i in range(1, k + 1):
            # n! / (n-k)!, because this part gets rid of the (n-k) numbers from n!
            fact *= n - i + 1

            # / k!
            fact //= i

        return fact


sol = Solution()
print(sol.uniquePaths(3, 7))
