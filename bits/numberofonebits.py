class Solution:
    def hammingWeight(self, n: int) -> int:
        val = 0

        while n: # n > 0
            val += 1
            n = n & (n-1)
        
        return val
        
sol = Solution()
print(sol.hammingWeight((0x00000000000000000000000000001011)))