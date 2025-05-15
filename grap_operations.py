from collections import deque

class GraphOperations:
    def find_edge(self, graph, from_node, to_node, representation):
        if representation == 'matrix':
            if 0 <= from_node < len(graph) and 0 <= to_node < len(graph):
                if graph[from_node][to_node] == 1:
                    return True, f"krawędź ({from_node},{to_node}) istnieje"
                return False, f"krawędź ({from_node},{to_node}) nie istnieje"
            return False, "Niepoprawny wierzchołek!"

        elif representation == 'list':
            if 0 <= from_node < len(graph):
                if to_node in graph[from_node]:
                    return True, f"krawędź ({from_node},{to_node}) istnieje"
                return False, f"krawędź ({from_node},{to_node}) nie istnieje"
            return False, "Niepoprawny wierzchołek!"

    def bfs(self, graph, start_node, representation):
        visited = []
        queue = deque([start_node])
        while queue:
            u = queue.popleft()
            if u not in visited:
                visited.append(u)
                if representation == 'matrix':
                    neighbors = [v for v, val in enumerate(graph[u]) if val == 1]
                else:
                    neighbors = graph[u]
                queue.extend(neighbors)
        return visited

    def dfs(self, graph, start_node, representation):
        visited = []
        stack = [start_node]
        while stack:
            u = stack.pop()
            if u not in visited:
                visited.append(u)
                if representation == 'matrix':
                    neighbors = [v for v, val in enumerate(graph[u]) if val == 1]
                else:
                    neighbors = graph[u]
                stack.extend(reversed(neighbors))
        return visited

    def topological_sort_kahn(self, graph, representation):
        n = len(graph)
        in_deg = [0] * n
        if representation == 'matrix':
            for u in range(n):
                for v, val in enumerate(graph[u]):
                    if val == 1: in_deg[v] += 1
            neigh = lambda u: [v for v, val in enumerate(graph[u]) if val == 1]
        else:
            for u in range(n):
                for v in graph[u]:
                    in_deg[v] += 1
            neigh = lambda u: graph[u]

        q = deque(i for i, d in enumerate(in_deg) if d == 0)
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in neigh(u):
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)
        if len(res) != n:
            raise ValueError("Graf zawiera cykl!")
        return res

    def topological_sort_tarjan(self, graph, representation):
        n = len(graph)
        state = [0] * n
        res = []

        def visit(u):
            if state[u] == 1:
                raise ValueError("Graf zawiera cykl!")
            if state[u] == 2:
                return
            state[u] = 1
            if representation == 'matrix':
                nbrs = [v for v, val in enumerate(graph[u]) if val == 1]
            else:
                nbrs = graph[u]
            for v in nbrs:
                visit(v)
            state[u] = 2
            res.append(u)

        for u in range(n):
            if state[u] == 0:
                visit(u)
        return res[::-1]