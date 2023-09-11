from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create adjacency matrix and edge list
        graph = [[0] * len(points) for i in range(len(points))]
        edges = {}

        for a, (x1, y1) in enumerate(points):
            for b, (x2, y2) in enumerate(points):
                cost = abs(x1 - x2) + abs(y1 - y2) if a != b else -1
                graph[a][b] = cost

                if (b, a) not in edges and a != b:
                    edges[(a, b)] = cost

        # sort the edges largest to smallest
        sorted_edges = sorted(
            zip(edges.keys(), edges.values()), key=lambda x: edges[x[0]], reverse=True
        )

        # remove edges if they are cyclic until we have
        edges_removed = 0
        ret = 0

        for (a, b), cost in sorted_edges:
            if edges_removed < len(points) + 1 and self.cycle(graph, b):
                edges_removed += 1
                graph[a][b] = -1
                graph[b][a] = -1
            else:
                ret += cost

        return ret

    def cycle(self, graph, edge) -> bool:
        visited = set()
        node = edge
        stack = [(i, node) for i in range(len(graph)) if graph[node][i] != -1]

        while stack:
            node, parent = stack.pop()

            if node == edge:
                return True
            else:
                if node not in visited:
                    # add all the children to the stack
                    stack += [
                        (i, node)
                        for i in range(len(graph))
                        if (graph[node][i] != -1 and i != parent)
                    ]

                    visited.add(node)

        return False  # went through all the nodes no cycle babyyy


sol = Solution()
print(sol.minCostConnectPoints(([[3, 12], [-2, 5], [-4, 1]])))
