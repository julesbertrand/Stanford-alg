import numpy as np
from collections import defaultdict
from tqdm import tqdm

from utils import timeit


@timeit(action_str=" Running Two sum alg ")
def two_sum(array, targets=(-10000, 10000)):
    H = defaultdict(set)
    res = set()
    print(" Hashing ".center(100, "-"))
    for x in tqdm(array):
        H[abs(x) // targets[1]].add(x)
    print(" Searching for targets ".center(100, "-"))
    for x in tqdm(array):
        h = abs(x) // targets[1]
        for y in H[h - 1].union(H[h]).union(H[h + 1]):
            if targets[0] <= x + y <= targets[1]:
                res.add(x + y)
    return len(res)


if __name__ == "__main__":
    A = np.loadtxt("./Course_2/2_sum.txt", dtype=float)
    n_targets_met = two_sum(A, targets=(-10000, 10000))
    print(n_targets_met)
