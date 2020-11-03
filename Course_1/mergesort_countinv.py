"""
### Merge sort
Complexity: 
- $6n$ operations per level
- $\log_2(n)$ recursive calls
- Total in time : $6n \log_2(n) + 6n = O(n\log(n))$
- In memory: $O(n)$ as need not in place

Inversions algorithm
Complexity: 
same as merge sort, $O(n\log(n))$ in time and $O(n)$ in memory
"""

import numpy as np


def merge_sort(A):
    def merge_sort_(A, l, r):
        if l < r:
            m = (l + r - 1) // 2
            merge_sort_(A, l, m)
            merge_sort_(A, m + 1, r)
            combine(A, l, m, r)

    def combine(A, l, m, r):
        n_l = m - l + 1
        n_r = r - m
        L = A[l : m + 1]
        R = A[m + 1 : r + 1]
        i, j, k = 0, 0, l
        while i < n_l and j < n_r:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < n_l:
            A[k] = L[i]
            k += 1
            i += 1
        while j < n_r:
            A[k] = R[j]
            k += 1
            j += 1

    return merge_sort_(A, 0, len(A) - 1)


def count_inversions(A):
    def sort_and_count_inversions(A, l, r):
        if r <= l:
            return 0
        else:
            m = (l + r - 1) // 2
            x = sort_and_count_inversions(A, l, m)
            y = sort_and_count_inversions(A, m + 1, r)
            z = combine_and_count_inv_split(A, l, m, r)
        return x + y + z

    def combine_and_count_inv_split(A, l, m, r):
        n_l = m - l + 1
        n_r = r - m
        L = A[l : m + 1]
        R = A[m + 1 : r + 1]
        i, j, k = 0, 0, l
        count = 0
        while i < n_l and j < n_r:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                count += n_l - i
                j += 1
            k += 1
        while i < n_l:
            A[k] = L[i]
            k += 1
            i += 1
        while j < n_r:
            A[k] = R[j]
            k += 1
            j += 1
        return count

    return sort_and_count_inversions(A, 0, len(A) - 1)


if __name__ == "__main__":
    A = np.loadtxt("./Course_1/countinv.txt").tolist()
    # A = [1, 23, 5, 2, 4, 6]
    count_inversions(A)
