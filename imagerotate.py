from typing import List
import numpy as np


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        # iterate to cut out an upper triangle then swap that triangle iteratively until rotate
        for y in range(N // 2):
            for x in range(y, N - y - 1):
                rot_x, rot_y = x, y

                for i in range(3):
                    matrix[rot_y][rot_x], matrix[-rot_x - 1][rot_y] = (
                        matrix[-rot_x - 1][rot_y],
                        matrix[rot_y][rot_x],
                    )
                    rot_x, rot_y = rot_y, -rot_x - 1


sol = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.rotate(matrix)
print(matrix)
