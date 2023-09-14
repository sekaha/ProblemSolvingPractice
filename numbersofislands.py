from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def check_neighbors(x, y):
            for x_off, y_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (0 <= y + y_off < len(grid)) and (0 <= x + x_off < len(grid[0])):
                    if (x + x_off, y + y_off) not in visited:
                        if grid[y + y_off][x + x_off] == "1":
                            visited.add((x + x_off, y + y_off))
                            check_neighbors(x + x_off, y + y_off)

        for y, row in enumerate(grid):
            for x, land in enumerate(row):
                if (x, y) not in visited:
                    visited.add((x, y))

                    if land == "1":
                        check_neighbors(x, y)
                        islands += 1

        check_neighbors(0, 0)

        return islands


sol = Solution()

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

print(sol.numIslands(grid))
