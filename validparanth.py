class Solution:
    def checkValidString(self, s: str) -> bool:
        specials = 0
        weight = 0

        for c in s:
            if c == "(":
                weight += 1
            elif c == ")":
                weight -= 1
            elif c == "*":
                specials += 1

        # balanced string, given the odd * rule
        return 0 in [weight + offset for offset in range(-specials, specials + 1)]
