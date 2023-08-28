class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}

        for str in strs:
            #somehow this is more efficient then not sorting it (i.e. manually going through and keeping track of letters)
            identifier = ''.join(sorted(str))
            
            if identifier in groups:
                groups[identifier].append(str)
            else:
                groups[identifier] = [str]

        return groups.values()

sol = Solution()

sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])