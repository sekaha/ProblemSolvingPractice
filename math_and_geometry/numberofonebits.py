class Solution:
    def hammingWeight(self, n: int) -> int:
        val = 0

        while n > 0:
            val += n&1
            n = n >> 1
        
        return val
        
sol = Solution()
sol.hammingWeight((0x00000000000000000000000000001011))