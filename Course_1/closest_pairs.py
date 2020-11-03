"""
### Closest pairs algorithm

Complexity:
- new recursive calls per call $a=2$.
- input size shrinkage $b=2$
- exponent on combine step $O(n)$ hence $d=1$
- Total: $a=b^d$ so $O(n\log(n))$
"""
import numpy as np
import random


class ClosestPair:
    """ Computes the closest pair of points in P """

    def closest_pair(self, P):
        n = len(P)
        if n <= 3:
            return self.brute_force_closest_pair(P)
        Px = sorted(P, key=lambda x: x[0])
        Py = sorted(P, key=lambda x: x[1])
        return self.closest_pair_(Px, Py, n)

    @staticmethod
    def dist(x, y):
        return np.linalg.norm(x - y)

    def brute_force_closest_pair(self, P):
        n = len(P)
        min_dist = float("inf")
        p, q = None, None
        for i in range(n - 1):
            for j in range(i + 1, n):
                d = self.dist(P[i], P[j])
                if min_dist > d:
                    min_dist = d
                    p, q = (P[i], P[j])
        return p, q, min_dist

    def closest_pair_(self, Px, Py, n):
        mid = n // 2
        if n <= 3:
            return self.brute_force_closest_pair(Px)
        Qx = Px[:mid]
        Rx = Px[mid:]
        Qy = []
        Ry = []
        mid_x = Px[mid][0]
        for p in Py:
            if p[0] <= mid_x:
                Qy.append(p)
            else:
                Ry.append(p)
        p1, q1, dist1 = self.closest_pair_(Qx, Qy, mid)
        p2, q2, dist2 = self.closest_pair_(Rx, Ry, n - mid)
        if dist1 <= dist2:
            best_pair = (p1, q1)
            best_dist = dist1
        else:
            best_pair = (p2, q2)
            best_dist = dist2
        p3, q3, dist3 = self.closest_pair_split(Px, Py, mid, best_dist, best_pair)
        return p3, q3, dist3

    def closest_pair_split(self, Px, Py, mid, best_dist, best_pair):
        x_bar = Px[mid - 1][0]  # biggest x_coord in left of P
        # S_y contains points with x-coord in [x_bar - best_dist, x_bar + best_dist]
        S_y = [p for p in Px if x_bar - best_dist <= p[0] <= x_bar + best_dist]
        n_S_y = len(S_y)
        for i in range(n_S_y - 1):
            for j in range(i + 1, min(i + 8, n_S_y)):
                p, q = S_y[i], S_y[j]
                d = self.dist(p, q)
                if d < best_dist:
                    best_dist = d
                    best_pair = (p, q)
        return best_pair[0], best_pair[1], best_dist


if __name__ == "__main__":

    def test_case(length: int = 10000, size: int = 100):
        Px = [random.randint(-size, size) for i in range(length)]
        Py = [random.randint(-size, size) for i in range(length)]
        P = np.array(list(zip(Px, Py)))
        return P

    P = test_case(length=10, size=1000)
    # print(P)

    # import matplotlib.pyplot as plt
    # plt.scatter(P[:, 0], P[:, 1])
    # plt.show()
    C = ClosestPair()
    print(C.closest_pair(P))
