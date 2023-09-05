stairs_memo = {0 : 0, 1 : 1, 2: 2}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n in stairs_memo:
            return stairs_memo[n]        
        
        v = self.climbStairs(n-1)+self.climbStairs(n-2)
        stairs_memo[n] = v
        return v

sol = Solution()
print(sol.climbStairs(44))