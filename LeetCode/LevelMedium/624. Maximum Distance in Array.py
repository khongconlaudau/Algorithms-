from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        largest = arrays[0][-1]
        distance = 0
        for i, arr in enumerate(arrays):
            if i == 0:
                continue
            distance = max(distance, (largest - arr[0]), (arr[-1] - smallest))
            smallest = min(smallest, arr[0])
            largest = max(largest, arr[-1])

        return distance

