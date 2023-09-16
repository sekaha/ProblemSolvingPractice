class Solution:
    def checkValidString(self, s: str) -> bool:
        min_lefts = 0
        max_lefts = 0

        for c in s:
            if c == "(":
                max_lefts += 1
                min_lefts += 1
            elif c == ")":
                max_lefts -= 1
                min_lefts -= 1
            else:
                min_lefts -= 1
                max_lefts += 1

            if min_lefts < 0:
                min_lefts = 0

            if max_lefts < 0:
                return False
                if min_lefts > 0:
                    min_lefts -= 1
        return min_lefts <= 0 <= max_lefts


sol = Solution()

print(sol.checkValidString("(*()))*("))
print(sol.checkValidString("*)*())"))
print(sol.checkValidString("(())"))
print(sol.checkValidString("))(("))
print(sol.checkValidString("()"))
print(sol.checkValidString("(*)"))
print(sol.checkValidString("(*))"))
print(sol.checkValidString("((*)"))

print(
    sol.checkValidString(
        "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
    )
)
