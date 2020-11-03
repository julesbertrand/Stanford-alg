import numpy as np
from collections import deque, defaultdict

from utils import timeit


@timeit(" Loading graph file ")
def load_graph(path="./SSC.txt"):
    return np.loadtxt(path, dtype=int)


class GraphUtils:
    def __init__(self, adj_list=None):
        if adj_list is not None:
            self.build_graph(adj_list)
            self.n = max(self.graph.keys())
        else:
            self.graph = defaultdict(list)
            self.n = 0

    def add_edge(self, u, v):
        if u not in self.graph.keys():
            self.n += 1
        self.graph[u].append(v)

    @timeit(action_str=" Building graph ")
    def build_graph(self, adj_list):
        self.graph = defaultdict(list)
        for u, v in adj_list:
            self.graph[u].append(v)
            self.graph[v]

    @timeit(action_str=" Transposing graph ")
    def get_transposed(self):
        g = Graph(adj_list=None)
        for u in self.graph:
            for v in self.graph[u]:
                g.graph[v].append(u)
                g.graph[u]
        return g


class Graph(GraphUtils):
    def __init__(self, adj_list):
        super().__init__(adj_list=adj_list)

    def BFS(self, s: int) -> None:
        explored = [False] * self.n
        Q = deque([s])
        explored[s - 1] = True
        while Q:
            v = Q.popleft()
            for w in self.graph[v]:
                if not explored[w - 1]:
                    explored[w - 1] = True
                    Q.append(w)

    def shortest_path(self, s: int) -> dict:
        """ BFS based shortest path """
        explored = [False] * self.n
        dist = {x: (float("inf") if x != s else 0) for x in self.graph.keys()}
        Q = deque([s])
        while Q:
            v = Q.popleft()
            for w in self.graph[v]:
                if not explored[w - 1]:
                    explored[w - 1] = True
                    dist[w] = dist[v] + 1
                    Q.append(w)
        return dist

    def connectivity(self) -> list:
        """ BFS based undirected connectivity components """
        explored = [False] * self.n
        connected_components = []
        for s in self.graph.keys():
            if not explored[s - 1]:
                # start BFS
                component = [s]
                Q = deque([s])
                explored[s - 1] = True
                while Q:
                    v = Q.popleft()
                    for w in self.graph[v]:
                        if not explored[w - 1]:
                            explored[w - 1] = True
                            component.append(w)
                            Q.append(w)
                connected_components.append(component)
        return connected_components

    def topo_sort_rec(self) -> dict:
        """ Returns topological ordering labels """
        self.explored = [False] * self.n
        self.current_label = self.n
        self.labels = defaultdict(int)
        for s in self.graph.keys():
            if not self.explored[s - 1]:
                self.__DFS_rec_helper(s)
        return self.labels

    def __DFS_rec_helper(self, s: int) -> None:
        """ Recursive DFS for topological sort"""
        self.explored[s - 1] = True
        for v in self.graph[s]:
            if not self.explored[v - 1]:
                self.__DFS_rec_helper(v)
                self.labels[v] = self.current_label
                self.current_label -= 1

    def topo_sort_iter(self):
        """ Compute topological ordering of nodes using iterative DFS """
        explored = [0] * self.n
        stack = deque()
        order = deque()
        for s in reversed(list(self.graph.keys())):
            if not explored[s - 1]:
                stack.append(s)
                while stack:
                    u = stack[-1]
                    if explored[u - 1]:
                        u = stack.pop()
                        if explored[u - 1] == 1:
                            order.append(u)
                            explored[u - 1] = 2
                    else:
                        explored[u - 1] = 1
                        for v in self.graph[u]:
                            if not explored[v - 1]:
                                stack.append(v)
        return order

    @timeit(" Running Strongly Connected Components ")
    def SCC(self):
        """ Compute Strongly connected components using iterative DGS """
        # same as topo iter
        explored = [0] * self.n
        stack = deque()
        order = deque()
        for s in reversed(list(self.graph.keys())):
            if not explored[s - 1]:
                stack.append(s)
                while stack:
                    u = stack[-1]
                    if explored[u - 1]:
                        u = stack.pop()
                        if explored[u - 1] == 1:
                            order.append(u)
                            explored[u - 1] = 2
                    else:
                        explored[u - 1] = 1
                        for v in self.graph[u]:
                            if not explored[v - 1]:
                                stack.append(v)

        g_rev = self.get_transposed()
        explored = [False] * self.n
        self.scc = []
        stack = deque()
        while order:
            s = order.pop()
            if not explored[s - 1]:
                stack.append(s)
                component = []
                while stack:
                    u = stack.pop()
                    if not explored[u - 1]:
                        explored[u - 1] = True
                        component.append(u)
                    for v in g_rev.graph[u]:  # looking at reverse graph
                        if not explored[v - 1]:
                            stack.append(v)
                self.scc.append(component)
        return self.scc


if __name__ == "__main__":
    G_np = load_graph("./Course_2/SCC.txt")
    g = Graph(G_np)

    # BFS
    g.shortest_path(1)

    # topological sort DFS
    g.topo_sort_iter()

    # strongly connected components
    scc = g.SCC()
    print(sorted(map(lambda x: len(set(x)), scc), reverse=True)[:10])
