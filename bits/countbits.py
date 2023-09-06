from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)

        for i in range(n+1):
            tmp = i

            while tmp:
                ans[i]+=1
                tmp &= (tmp-1)

        return ans