class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return false
        letters = set(s1 + s2)
        s1_count = {c: 0 for c in letters}
        s2_count = {c: 0 for c in letters}

        # determining initial matches of first window
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1

        matches = sum([s1_count[c] == s2_count[c] for c in letters])

        l, r = 0, len(s1)

        while r < len(s2):
            if matches == len(letters):
                return True

            # adjust for inclusion of right element
            s2_count[s2[r]] += 1

            if s1_count[s2[r]] == s2_count[s2[r]]:  # was not matching, now is
                matches += 1
            elif s1_count[s2[r]] + 1 == s2_count[s2[r]]:  # was matching, no longer is
                matches -= 1

            # adjust for removal of left element
            s2_count[s2[l]] -= 1

            if s1_count[s2[l]] == s2_count[s2[l]]:  # was not matching, now is
                matches += 1
            elif s1_count[s2[l]] - 1 == s2_count[s2[l]]:  # was matching, no longer is
                matches -= 1

            l += 1
            r += 1
        return matches == len(letters)


sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))
