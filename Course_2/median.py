import numpy as np
from tqdm import tqdm
import heapq

from utils import timeit


class MedianMaintenance:
    def __init__(self, nums=[]):
        self.nums = nums
        self.heap_low = []
        self.heap_high = []
        self.same_heap_length = True

    def insert(self, num):
        self.nums.append(num)
        if not self.heap_low:
            heapq.heappush(self.heap_low, -num)
            self.same_heap_length = False
        elif num <= -self.heap_low[0]:  # below or equal to median
            if self.same_heap_length == True:
                heapq.heappush(self.heap_low, -num)
                self.same_heap_length = False
            else:  # too much elements in heap_low
                new_num = -heapq.heappushpop(self.heap_low, -num)
                heapq.heappush(self.heap_high, new_num)
                self.same_heap_length = True
        else:  # above median
            if self.same_heap_length == True:  # heap_low must always contain median
                new_num = heapq.heappushpop(self.heap_high, num)
                heapq.heappush(self.heap_low, -new_num)
                self.same_heap_length = False
            else:  # complete heap_high
                heapq.heappush(self.heap_high, num)
                self.same_heap_length = True

    def median(self):
        median = -self.heap_low[0]
        return median


if __name__ == "__main__":
    data = np.loadtxt("./median.txt", dtype=int)
    medians = []
    verif = []
    m = MedianMaintenance(nums=[])
    for num in tqdm(data, total=len(data)):
        m.insert(num)
        medians.append(m.median())
        verif.append(sorted(m.nums)[(len(m.nums) + 1) // 2 - 1])
        if medians[-1] != verif[-1]:
            print(sorted(m.nums))
            print(medians[-1])
            print(verif[-1])
            print(m.heap_high, m.heap_low)
            break
