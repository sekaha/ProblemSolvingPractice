from math import ceil, floor
class Solution(object):


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left <= right:
            i = left+(right-left)//2

            if nums[i] == target:
                return i
            
            if nums[i] < target:
                left = i+1
            else:
                right = i-1
        return -1

sol = Solution()
print(sol.search([-1,0,5],5))