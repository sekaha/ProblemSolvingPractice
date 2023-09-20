from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = list(range(len(edges) + 1))
        tree_size = [1] * (len(edges) + 1)  # rank

        def find(n):
            if par[n] != n:
                par[n] = find(par[n])  # path compression
            return par[n]

        def union(a, b):
            p1, p2 = find(a), find(b)

            if p1 == p2:  # can't union because they're already in the same tree
                return False

            if tree_size[p1] > tree_size[p2]:
                p1, p2 = p2, p1
            par[p1] = p2
            tree_size[p2] += tree_size[p1]
            return True

        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]

        return []


sol = Solution()
print(sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
print(sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
print(sol.findRedundantConnection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]))
