from typing import List
import numpy as np


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = 10  # len(matrix)
        test = [[0] * N for n in range(N)]
        visited = set()

        for x in range(N):
            for y in range(N):
                if (x, y) not in visited:
                    test[x][y] = 1

                    cur_x, cur_y = x, y

                    for i in range(4):
                        visited.add((cur_x, cur_y))
                        # application of 90 deg rotation matrix, plus some tomfoolery since we have to do zero indexing
                        cur_x, cur_y = (N - cur_y - 1), cur_x

        test2 = [[0] * N for n in range(N)]

        for y in range(N // 2):
            for x in range(y, N - y - 1):
                test2[y][x] = 1

        test, test2 = np.array(test), np.array(test2)

        print(np.array_equal(test, test2))


sol = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.rotate(matrix)
