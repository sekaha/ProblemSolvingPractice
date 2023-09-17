from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            # If the current number is within the valid range and not in its correct position
            if nums[i] < n and nums[i] != nums[nums[i]]:
                # Swap the current number with the number at its correct position
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1

        # Find the first number that is not in its correct position, which is the missing number
        for i in range(n):
            if nums[i] != i:
                return i

        # If all numbers are in their correct positions, then n is the missing number
        return n


sol = Solution()
print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
# print(
#    sol.missingNumber(
#        [
#            45,
#            35,
#            38,
#            13,
#            12,
#            23,
#            48,
#            15,
#            44,
#            21,
#            43,
#            26,
#            6,
#            37,
#            1,
#            19,
#            22,
#            3,
#            11,
#            32,
#            4,
#            16,
#            28,
#            49,
#            29,
#            36,
#            33,
#            8,
#            9,
#            39,
#            46,
#            17,
#            41,
#            7,
#            2,
#            5,
#            27,
#            20,
#            40,
#            34,
#            30,
#            25,
#            47,
#            0,
#            31,
#            42,
#            24,
#            10,
#            14,
#        ]
#    )
# )
#
