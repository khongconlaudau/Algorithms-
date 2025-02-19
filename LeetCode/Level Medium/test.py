from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost = 0
        travelFrom = n - k
        if len(times) == 0:
            return -1
        if len(times) == 1:
            if times[0][0] != k:
                return -1
            else:
                return times[0][2]

        if travelFrom >= k:
            for i in range(len(times)):
                if times[i][0] == k and times[i][0] < times[i][1]:
                    cost += times[i][2]
                    k = times[i][1]
        else:
            for i in range(len(times)):
                if times[i][0] == k and times[i][0] > times[i][1]:
                    cost += times[i][2]
                    k = times[i][1]
        return cost
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
sol = Solution()
print(sol.networkDelayTime(times, n, k))