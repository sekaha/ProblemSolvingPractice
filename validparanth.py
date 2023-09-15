class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def backtracking(i=0, weight=0):
            if i == len(s):
                return weight == 0

            if (i, weight) in memo:
                return memo[i, weight]
            else:
                if s[i] == "(":
                    validity = backtracking(i + 1, weight + 1)

                if s[i] == ")":
                    if weight > 0:
                        validity = backtracking(i + 1, weight - 1)
                    else:
                        validity = False

                if s[i] == "*":
                    validity = backtracking(i + 1, weight + 1)

                    if weight > 0:
                        validity |= backtracking(i + 1, weight - 1)

                    validity |= backtracking(i + 1, weight)

                memo[(i, weight)] = validity

                return validity

        return backtracking()


sol = Solution()

print(sol.checkValidString("(*()))*("))
print(sol.checkValidString("*)*())"))
print(sol.checkValidString("()"))
print(sol.checkValidString("(*)"))
print(sol.checkValidString("(*))"))
print(sol.checkValidString("((*)"))

print(
    sol.checkValidString(
        "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
    )
)
