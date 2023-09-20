from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        stack1, stack2 = [], []
        answers = []

        def split(i=0):
            if i == len(nums):
                if sum(stack1) == sum(stack2):
                    answers.append((stack1.copy(), stack2.copy()))
                return

            for s in stack1, stack2:
                s.append(nums[i])
                split(i + 1)
                s.pop()

        split()
        print(answers)

        # def split(i=0):
        #    if i == len(nums) and (sum(stack1) == sum(stack2)):
        #        yield (stack1.copy(), stack2.copy())
        #    for j in range(i, len(nums)):
        #        for stack in (stack1, stack2):
        #            stack.append(nums[j])
        #            yield from split(i + 1)
        #            stack.pop()

        # print(list(split()))


sol = Solution()
sol.canPartition([1, 5, 11, 5])
