"""
Karatsuba multiplication implementation
Complexity:
- recursive calls: $a=3$ per call
- input size shrinkage $b=2$ (divide by each call)
- combine step $O(n)$ hence $d=1$
- finally $a=3 > b^d=2$ hence $O(n^{\log(3)})$.
"""


def karatsuba_mul(x, y):
    x, y = str(x), str(y)
    n_x, n_y = len(x), len(y)
    if n_x == n_y == 1:
        return int(x) * int(y)
    elif n_x < n_y:
        x = "0" * (n_y - n_x) + x
    elif n_y < n_x:
        y = "0" * (n_x - n_y) + y
    n = len(x)
    mid = n // 2
    if n % 2 != 0:
        mid += 1
    a, b = int(x[:mid]), int(x[mid:])
    c, d = int(y[:mid]), int(y[mid:])
    ac = karatsuba_mul(a, c)
    bd = karatsuba_mul(b, d)
    k = karatsuba_mul(a + b, c + d) - ac - bd
    return int(str(ac) + "0" * (n - mid) * 2) + int(str(k) + "0" * (n - mid)) + int(bd)


if __name__ == "__main__":
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    print(karatsuba_mul(x, y))
    print(karatsuba_mul(x, y) == x * y)
