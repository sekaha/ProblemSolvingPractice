class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        max_num = 10 ** n - 1
        min_num = 10 ** (n - 1)

        for num in range(int(max_num), int(min_num) - 1, -1):
            # Construct a palindrome by joining num with its reverse
            palindrome = int(str(num) + str(num)[::-1])

            # Check if this palindrome can be represented as the product of two n-digit integers
            for i in range(max_num, int(palindrome ** 0.5) - 1, -1):
                if palindrome % i == 0 and palindrome // i <= max_num:
                    return palindrome % 1337

sol = Solution()

for n in range(1,9):
    print(sol.largestPalindrome(n))