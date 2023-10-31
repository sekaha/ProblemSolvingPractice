class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        memo = {}

        def helper(p1, p2, p3):
            if (p1, p2, p3) in memo:
                return memo[(p1, p2, p3)]

            if (p1 == len(s1)) and (p2 == len(s2)) and (p3 == len(s3)):
                memo[(p1, p2, p3)] = True
                return True

            if p3 >= len(s3):
                memo[(p1, p2, p3)] = False
                return False

            valid = False

            # split possibility cases basically
            if p1 < len(s1):
                if s1[p1] == s3[p3]:
                    valid |= helper(p1 + 1, p2, p3 + 1)

            if not valid:
                if p2 < len(s2):
                    if s2[p2] == s3[p3]:
                        valid |= helper(p1, p2 + 1, p3 + 1)

            memo[(p1, p2, p3)] = valid
            return valid

        return helper(0, 0, 0)
