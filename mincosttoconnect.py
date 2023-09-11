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

        # while there's still a cycle, remove the largest edge until there is not
        i = 0
        edges_removed = 0
        ret = 0

        # while i < len(sorted_edges):
        #    (a, b), v = sorted_edges[i]
        #
        #    if edges_removed < len(points) + 1:
        #        if self.cycle(graph, a) or self.cycle(graph, b):
        #            edges_removed += 1
        #            graph[a][b] = -1
        #        else:
        #            ret += v
        #    else:
        #        print((a, b))
        #        ret += v
        #
        #    i += 1

        for (a, b), cost in sorted_edges:
            if edges_removed < len(points) + 1:
                if self.cycle(graph, a):  # or self.cycle(graph, b):
                    edges_removed += 1
                    graph[a][b] = -1
                    graph[b][a] = -1
                else:
                    print(f"({a},{b})", cost)
                    ret += cost
            else:
                print(f"({a},{b})", cost)
                ret += cost
        print(ret)
        return ret

    def cycle(self, graph, edge) -> bool:
        visited = set()
        node = edge
        stack = [(i, node) for i in range(len(graph)) if graph[node][i] != -1]

        while stack:
            node, parent = stack.pop()

            if node == edge:
                print("found")
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

        print("cleared")
        return False  # went through all the nodes no cycle babyyy


sol = Solution()
sol.minCostConnectPoints(([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
