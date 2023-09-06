from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        ans = [0]*(n+1)

        for i in range(1,n+1):
            if i == offset*2:
                offset *= 2
            
            ans[i] = 1+ans[i-offset]

        return ans