from typing import List
import numpy as np

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        arr = np.array(matrix)
        count = 1
        m, n = arr.shape
        for i in range(m):
            if i == m - 1:
                break
            fliparr = (arr[i] == 0).astype(int)
            for k in range(i+1, m):
                if np.array_equal(fliparr, arr[k]):
                    count += 1
        return count

# arr = np.array([[0,1],[1,1]])
# print((arr[0] == 0).astype(int))
sol = Solution()
print(sol.maxEqualRowsAfterFlips([[0,1],[1,1]]))