from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = [False] * len(edges)

        for e in edges:
            v1, v2 = e
            if visited[v1 - 1] and visited[v2 - 1]:
                return e
            visited[v1 - 1], visited[v2 - 1] = True, True


sol = Solution()
print(sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
print(sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
print(sol.findRedundantConnection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]))
