class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n_seen = {}

        for i, n in enumerate(nums):
            pair = (target-n)
            
            if pair in n_seen:
                return [n_seen[pair],i]

            # this is fine since there's an assumption there's only one solution
            n_seen[n] = i

s = Solution()

print(s.twoSum([3,2,4],6))