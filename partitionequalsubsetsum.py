from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # what num we're on in the list
        # which list was last added to
        summation = sum(nums)
        halfsum = summation // 2

        if summation % 2:
            return False

        traversed = [(0, halfsum)]

        while traversed:
            index, target = traversed.pop()

            if index < len(nums):
                if target - nums[index] == 0:
                    return True

                if nums[index] < target:
                    traversed.append((index + 1, target - nums[index]))
                traversed.append((index + 1, target))

        return False


sol = Solution()
print(sol.canPartition([14, 9, 8, 4, 3, 2]))
