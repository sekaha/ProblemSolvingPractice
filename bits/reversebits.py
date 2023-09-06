class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0

        for i in range(32):
            output = output << 1
            output += 1 & n
            n = n >> 1
        
        return output

sol = Solution()
print(sol.reverseBits((0b00000010100101000001111010011100)))