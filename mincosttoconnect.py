from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create adjacency matrix and edge list
        edges = {}

        for a, (x1, y1) in enumerate(points):
            for b, (x2, y2) in enumerate(points):
                if (b, a) not in edges and a != b:
                    cost = abs(x1 - x2) + abs(y1 - y2) if a != b else -1
                    edges[(a, b)] = cost

        # sort the edges largest to smallest
        sorted_edges = sorted(
            zip(edges.keys(), edges.values()), key=lambda x: edges[x[0]]
        )

        # add edges if they do not form cycle
        graph = [[-1 for a in range(len(points))] for b in range(len(points))]
        edges = 0
        ret = 0

        for (a, b), cost in sorted_edges:
            if edges < len(points) - 1:
                graph[a][b] = cost
                graph[b][a] = cost

                if self.cycle(graph, b):
                    graph[a][b] = -1
                    graph[b][a] = -1
                else:
                    edges += 1
                    ret += cost

        return ret

    def cycle(self, graph, edge) -> bool:
        visited = set()
        node = edge
        stack = [(i, node) for i in range(len(graph)) if graph[node][i] != -1]

        # cycle not detecting correctly gr
        while stack:
            node, parent = stack.pop()

            if node not in visited:
                # add all the children to the stack
                stack += [
                    (i, node)
                    for i in range(len(graph))
                    if (graph[node][i] != -1 and i != parent)
                ]

                visited.add(node)
            else:
                return True
        return False  # went through all the nodes no cycle babyyy


sol = Solution()
# should be 102....
print(sol.minCostConnectPoints([[-1000000, -1000000], [1000000, 1000000]]))
