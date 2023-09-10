from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(left,right="",out=""):
            if left:
                if right:
                    for push in range(2):
                        if push:
                            yield from gen(left[1:],right+")",out+"(")
                        else:
                            yield from gen(left,right[1:],out+")")
                else:
                    yield from gen(left[1:],right+")",out+"(")
            else:
                yield out+right

        return list(gen("("*n))

sol = Solution()
print(sol.generateParenthesis(3))