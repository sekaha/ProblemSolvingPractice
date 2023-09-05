class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            n = sum([int(c)**2 for c in str(n)])
            
            if n in seen:
                return False
            
            if n == 1:
                return True

            seen.add(n)

sol = Solution()
print(sol.isHappy((7)))