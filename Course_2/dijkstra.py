import time
from collections import defaultdict
import heapq
from tqdm import tqdm

from utils import timeit


@timeit(" Loading graph file ")
def open_dijkstra(path="./Course_2/Dijkstra.txt"):
    with open(path) as file:
        G_lst = []
        for row in file:
            row = row.split()
            G_lst.append(row)
    return G_lst


class Graph:
    def __init__(self, adj_list=None):
        self.build_graph(adj_list)
        self.n = max(self.graph.keys())

    @timeit(" Building graph ")
    def build_graph(self, adj_list):
        self.graph = defaultdict(list)
        for row in adj_list:
            key = int(row[0])
            for edge in row[1:]:
                node, dist = map(int, edge.split(","))
                self.graph[key].append((node, dist))
                self.graph[node]

    @timeit("Transposing graph ")
    def get_transposed(self):
        g = Graph()
        # Recur for all the vertices adjacent to this vertex
        for u in self.graph:
            for v in self.graph[u]:
                g.graph[u].append(v)
        return g

    def dijkstra(self, s):
        explored = defaultdict(bool)
        dist = {key: float("inf") for key in self.graph.keys()}
        dist[s] = 0
        spt = defaultdict(list)
        for _ in self.graph.keys():
            # looking for closest vertex
            min_dist = float("inf")
            for v in self.graph.keys():
                if dist[v] < min_dist and not explored[v]:
                    min_dist = dist[v]
                    u = v
            # u is always s in first iteration
            explored[u] = True

            for v, d in self.graph[u]:
                if not explored[v] and dist[v] > dist[u] + d:
                    dist[v] = dist[u] + d
                    spt[v] = spt[u] + [u]
        return dist, spt

    def dijkstra_heap(self, s):
        explored = defaultdict(bool)
        dist = {key: float("inf") for key in self.graph.keys()}
        dist[s] = 0
        spt = defaultdict(list)
        q = [(0, s)]  # dist, node, pred
        for _ in self.graph.keys():
            # looking for closest vertex
            _, u = heapq.heappop(q)
            explored[u] = True
            for v, d in self.graph[u]:
                if not explored[v] and dist[v] > dist[u] + d:
                    dist[v] = dist[u] + d
                    spt[v] = spt[u] + [u]
                    heapq.heappush(q, (dist[v], v))
        return dist, spt


def compare_times(G_lst: list, n: int = 100):
    """
    Takes graph and sampling time n, and compute dijkstra for all nodes to all nodes n times
    returns avg time per iter
    """

    @timeit(" Starting comparison ")
    def compare_times_(func):
        start_time = time.time()
        for _ in tqdm(range(n), total=n):
            for i in range(1, g.n):
                func(i)
        print(
            "Avg time for {}: {}".format(func.__name__, (time.time() - start_time) / n)
        )

    g = Graph(G_lst)
    for func in [g.dijkstra, g.dijkstra_heap]:
        compare_times_(func)


if __name__ == "__main__":
    G_lst = open_dijkstra()
    compare_times(G_lst, n=100)
