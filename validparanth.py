class Solution:
    def checkValidString(self, s: str) -> bool:
        weight = 0
        latent = 0

        for c in s:
            if c == "(":
                weight += 1
            elif c == ")":
                if weight > 0:
                    weight -= 1
                else:
                    if latent <= 0:
                        return False
                    else:
                        latent -= 1

            elif c == "*":
                latent += 1

        return weight == 0


sol = Solution()

print(sol.checkValidString("(("))
print(sol.checkValidString("()"))
print(sol.checkValidString("(*)"))
print(sol.checkValidString("(*))"))
print(sol.checkValidString("((*)"))

# print(
#    sol.checkValidString(
#        "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
#    )
# )
