class Solution:
    def uniquePaths(self, w: int, h: int) -> int:
        # finding the simplex numbers (natural, triangular, tetrahedral...)  depending on inputs
        n, k = h + w - 2, w - 1
        result = 1

        # n choose k
        for i in range(k):
            # n! / (n-k)!, because this part gets rid of the (n-k) numbers from n!
            result *= n - i

            # / k!
            result //= i + 1

        return result


sol = Solution()
print(sol.uniquePaths(3, 7))
