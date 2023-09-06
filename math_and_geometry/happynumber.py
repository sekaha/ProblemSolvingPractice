class Solution:
    def isHappy(self, n: int) -> bool:
        sum_squared_digits = lambda x: sum([int(c)**2 for c in str(x)])
        slow = n
        fast = sum_squared_digits(n)

        while fast!=slow:
            fast = sum_squared_digits(fast)
            fast = sum_squared_digits(fast)
            slow = sum_squared_digits(slow)

        return fast == 1


sol = Solution()
print(sol.isHappy((2)))