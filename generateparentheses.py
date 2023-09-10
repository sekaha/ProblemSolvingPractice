from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(left,right,out=""):
            if not left and not right:
                yield out
            if left:
                yield from gen(left-1,right,out+"(")
            if right > left:
                yield from gen(left,right-1,out+")")
        
        return list(gen(n,n))

sol = Solution()
print(sol.generateParenthesis(3))