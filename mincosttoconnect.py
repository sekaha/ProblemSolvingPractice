from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create adjacency list
        #graph = {}
        graph = 

        #for a, (x1, y1) in enumerate(points):
        #    for b, (x2, y2) in enumerate(points):
        #        if a != b and (b, a) not in graph:
        #            graph[(a, b)] = abs(x1 - x2) + abs(y1 - y2)
        #
        ## sort the graph by its edges and remove until there are no cycles
        #sorted_edges = sorted(graph.keys(), key=lambda x: graph[x])

        #while cycle():
        #    node = sorted_edges[-1]
        #    graph.remove(node)

        return graph

    def cycle(self, graph) -> bool:
        # DFS + visited
        slow = 
        fast = 


sol = Solution()
sol.minCostConnectPoints(([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
