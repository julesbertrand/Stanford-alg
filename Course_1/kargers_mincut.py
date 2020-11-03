import numpy as np
import pandas as pd
import math
import random
import copy
from tqdm import tqdm


def mincut(V, n=None):
    """ Run karger's algorithms n times to try to find the number of crossing edges in the mincut """

    def kargers(V):
        while len(V) > 2:
            v1 = random.choice(list(V.keys()))
            v2 = random.choice(V[v1])
            for x in V[v2]:
                if x != v1:
                    V[x].remove(v2)
                    V[x].append(v1)
                    V[v1].append(x)
            while v2 in V[v1]:
                V[v1].remove(v2)
            del V[v2]
        return len(list(V.values())[0])

    if not n:
        n = len(V) ** 2 * int(np.log(len(V)))
    min_crossing = len(V)
    for _ in tqdm(range(n), total=n):
        G = copy.deepcopy(V)
        k = kargers(G)
        min_crossing = min(k, min_crossing)
    return min_crossing


if __name__ == "__main__":
    V_txt = pd.read_csv(
        "./Course_1/KargerMinCut.txt",
        delimiter="\t",
        names=[str(i) for i in range(100)],
    ).values.tolist()
    V = {}
    for i in range(len(V_txt)):
        vertex = int(V_txt[i][0])
        V[vertex] = [int(x) for x in V_txt[i][1:] if not math.isnan(x)]
    min_edges = mincut(V, n=200 ** 2)
    print(min_edges)
