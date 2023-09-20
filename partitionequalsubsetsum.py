from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # what num we're on in the list
        # which list was last added to
        partition1, partition2 = [], []
        stack = [(0, 0)]

        while stack:
            print(partition1, partition2)
            i, partition = stack.pop()

            if i == len(nums):
                if sum(partition1) == sum(partition2):
                    return True
            else:
                if partition == 0:
                    partition1.append(nums[i])
                elif partition == 1:
                    partition2.append(nums[i])
                    partition1.pop()
                elif partition == 2:
                    partition2.pop()

                if partition < 2:
                    stack.append((i, partition + 1))

                stack.append((i + 1, 0))

        split()
        print(answers)


sol = Solution()
print(sol.canPartition([1, 5, 11, 5]))
