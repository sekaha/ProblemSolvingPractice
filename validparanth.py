class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []

        def backtracking(s):
            validity = False

            if len(s) == 0:
                return len(stack) == 0

            # if the char is ( or can be swapped for (
            c = "(" if s[0] == "*" else s[0]

            if c == "(":
                stack.append("(")
                validity |= backtracking(s[1:])
                stack.pop()

            # if the char is ) or can be swapped for )
            c = ")" if s[0] == "*" else s[0]

            if c == ")":
                if len(stack) > 0:
                    stack.pop()
                    validity |= backtracking(s[1:])
                    stack.append("(")
                else:
                    return False

            # if the char is * and we should explore a route where it's ignored
            if s[0] == "*":
                validity |= backtracking(s[1:])

            return validity

        return backtracking(s)


sol = Solution()

print(sol.checkValidString("(("))
print(sol.checkValidString("()"))
print(sol.checkValidString("(*)"))
print(sol.checkValidString("(*))"))
print(sol.checkValidString("((*)"))

print(
    sol.checkValidString(
        "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
    )
)
