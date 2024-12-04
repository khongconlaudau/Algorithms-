from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tempSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            tempSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, tempSum)

        return maxSum / k
