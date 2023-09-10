from typing import List
from time import time


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []

        def gen(left, right):
            if not left and not right:
                yield "".join(stack)
            if left:
                stack.append("(")
                yield from gen(left - 1, right)
                stack.pop()
            if right > left:
                stack.append(")")
                yield from gen(left, right - 1)
                stack.pop()

        return list(gen(n, n))


sol = Solution()

start = time()
sol.generateParenthesis(12)
print(time() - start)
