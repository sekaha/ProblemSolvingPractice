from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = {}

        for a, (x1, y1) in enumerate(points):
            for b, (x2, y2) in enumerate(points):
                if a != b:
                    if (b, a) in costs:
                        costs[a, b] = costs[b, a]
                    else:
                        costs[a, b] = abs(x1 - x2) + abs(y1 - y2)

        remaining = [i for i in range(len(points) - 1)]
        added = [len(points) - 1]
        cost = 0

        while remaining:
            min_edge_v = 10**7
            min_edge = -1

            for i in remaining:
                for j in added:
                    if costs[i, j] < min_edge_v:
                        min_edge_v = costs[i, j]
                        min_edge = i

            cost += min_edge_v
            remaining.remove(min_edge)
            added.append(min_edge)

        return cost


sol = Solution()
print(sol.minCostConnectPoints([[-1000000, -1000000], [1000000, 1000000]]))
