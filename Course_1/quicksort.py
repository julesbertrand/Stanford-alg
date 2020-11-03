"""
## Week 3: Quick sort

Complexity:
- with first element pivot: averge $O(n\log(n))$, worst case $O(n^2)$
- with median element pivot: always $O(n\log(n))$
- with random pivot: average $O(n\log(n))$
- Memory complexity: $O(1)$ in place 
- sometimes unstable
"""
import numpy as np
import random


class QuickSorter:
    def __init__(self, pivot_type="median_of_three"):
        self._params = {}
        self.pivot_type = pivot_type

    def sort(self, A):
        """ Quicksort initialization and accessible function to the user """
        self.data = A
        l, r = 0, len(self.data) - 1
        self.count = 0
        self.__quicksort(l, r)
        self.data = None
        return self.count

    def __quicksort(self, l, r):
        """ Quicksort algorithm """
        if l < r:
            p_idx = self.__pivot(l=l, r=r)
            p_idx = self.__partition(l, r, p_idx)
            self.count += r - l
            self.__quicksort(l=l, r=p_idx - 1)
            self.__quicksort(l=p_idx + 1, r=r)

    def __partition(self, l, r, p_idx):
        """ Partition step for quicksort """
        pivot = self.data[p_idx]
        self.data[p_idx], self.data[l] = self.data[l], self.data[p_idx]
        i = l + 1
        for j in range(l + 1, r + 1):
            if self.data[j] < pivot:
                self.data[j], self.data[i] = self.data[i], self.data[j]
                i += 1
        self.data[i - 1], self.data[l] = self.data[l], self.data[i - 1]
        return i - 1

    @property
    def pivot_type(self):
        return self._params["pivot_type"]

    @pivot_type.setter
    def pivot_type(self, pivot_type="median_of_3"):
        """ Set pivot type and pivot function """
        if pivot_type == "median_of_three":
            self.__pivot = self.__median_of_three  # median of three rule for pivot
        elif pivot_type == "random":
            self.__pivot = self.__random_pivot  # random pivot selection
        elif pivot_type == "first":
            self.__pivot = self.__first_element  # pivot is fisrt element
        elif pivot_type == "last":
            self.__pivot = self.__last_element  # pivot is last element
        else:
            raise ValueError("This pivot type does not exist")
        self._params["pivot_type"] = pivot_type

    @staticmethod
    def __first_element(l, r):
        """ Pivot selection: lefter element"""
        return l

    @staticmethod
    def __last_element(l, r):
        """ Pivot selection: righter element"""
        return r

    @staticmethod
    def __random_pivot(l, r):
        """ Pivot selection: random pivot """
        return random.randint(l, r)

    def __median_of_three(self, l, r):
        """ pivot selection: median of left, right, and middle elements """
        m = (l + r) // 2
        a = self.data[l]
        b = self.data[m]
        c = self.data[r]
        if a <= b <= c or c <= b <= a:
            return m
        if a <= c <= b or b <= c <= a:
            return r
        return l


class LinearSelection:
    """
    Output the i-th statistic of a list
    Random and Deterministic selection of pivot
    """

    def __init__(self, pivot_type):
        self.params = {}
        self.pivot_type = pivot_type

    @property
    def pivot_type(self):
        return self.params["pivot_type"]

    @pivot_type.setter
    def pivot_type(self, pivot_type):
        """ Set pivot type and pivot function """
        if pivot_type in "rd":
            self.params["pivot_type"] = pivot_type
        else:
            raise ValueError("This pivot type does not exist")

    def linear_selection(self, A, i, pivot_type=None):
        """ Initialization and choose R or D select"""
        self.data = A
        l, r = 0, len(self.data) - 1
        if pivot_type:
            self.pivot_type = pivot_type
        if self.pivot_type == "r":
            res = self.__R_select(l, r, i)
        if self.pivot_type == "d":
            res = self.__D_select(l, r, i)
        return res

    def __R_select(self, l, r, i):
        """ Randomized Linear selection algorithm """
        if i - 1 > r:
            raise KeyError
        elif l == r:
            return A[l]
        elif l < r:
            p_idx = random.randint(l, r - 1)
            p_idx = self.__partition(l, r, p_idx)
            if p_idx == i - 1:
                return A[p_idx]
            elif p_idx > i - 1:
                return self.__R_select(l, p_idx - 1, i)
            else:
                return self.__R_select(p_idx + 1, r, i)

    def __D_select(self, l, r, i):
        """ Deterministic Linear selection algorithm """
        #         if i > r:
        #             raise KeyError
        #         elif l == r:
        #             return A[l]
        #         elif l < r:
        #             n = r - l
        #             n_C = n // 5 + n % 5
        #             C = [sorted(self.data[i:i+5])[2] for i in range(l, r ,5)]
        #             p_idx = self.__D_select(C, None, None)
        #             p_idx = self.__partition(l, r, p_idx)
        #             if p_idx == i - 1:
        #                 return A[p_idx]
        #             elif p_idx > i - 1:
        #                 return self.__D_selection(l, p_idx - 1, i)
        #             else:
        #                 return self.__D_selection(p_idx + 1, r, i)
        raise NotImplementedError

    def __partition(self, l, r, p_idx):
        """Partition step for linear selection (same as for quicksort) """
        pivot = self.data[p_idx]
        self.data[p_idx], self.data[l] = self.data[l], self.data[p_idx]
        i = l + 1
        for j in range(l + 1, r + 1):
            if self.data[j] < pivot:
                self.data[j], self.data[i] = self.data[i], self.data[j]
                i += 1
        self.data[i - 1], self.data[l] = self.data[l], self.data[i - 1]
        return i - 1


if __name__ == "__main__":
    # Quicksort
    pivot_type = "last"
    q = QuickSorter(pivot_type=pivot_type)
    A = np.loadtxt("./Course_1/quicksort.txt").tolist()
    # print(A)
    print(
        'Count of comparison made when running quisksort with pivot "{}": {}'.format(
            pivot_type, q.sort(A)
        )
    )

    # Linear selection
    l = LinearSelection(pivot_type="r")
    A = np.loadtxt("./Course_1/quicksort.txt").tolist()
    i = 1000
    print(l.linear_selection(A, i))
